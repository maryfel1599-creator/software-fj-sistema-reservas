"""
Archivo: reserva.py

Este módulo contiene la clase Reserva, encargada de relacionar
un cliente con un servicio solicitado.
"""

# Se importa Enum para definir estados controlados.
from enum import Enum

# Se importa la clase abstracta general.
from entidad import EntidadSistema

# Se importan las clases Cliente y Servicio.
from cliente import Cliente
from servicios import Servicio

# Se importan excepciones relacionadas con reservas.
from excepciones import (
    DuracionInvalidaError,
    EstadoReservaError,
    ServicioNoDisponibleError
)

# Se importan funciones para registrar eventos.
from configuracion_log import registrar_evento


# Se crea una enumeración con los estados permitidos.
class EstadoReserva(Enum):
    """
    Define los estados disponibles de una reserva.
    """

    PENDIENTE = "Pendiente"
    CONFIRMADA = "Confirmada"
    PROCESADA = "Procesada"
    CANCELADA = "Cancelada"


# Se crea la clase Reserva.
class Reserva(EntidadSistema):
    """
    Representa una reserva de un servicio realizada por un cliente.
    """

    def __init__(self, codigo, cliente, servicio, duracion):
        """
        Inicializa una reserva en estado pendiente.
        """

        # Se llama al constructor de la clase padre.
        super().__init__(codigo)

        # Se valida que el cliente sea del tipo correcto.
        if not isinstance(cliente, Cliente):
            raise TypeError(
                "El cliente debe ser una instancia de Cliente."
            )

        # Se valida que el servicio sea del tipo correcto.
        if not isinstance(servicio, Servicio):
            raise TypeError(
                "El servicio debe ser una instancia de Servicio."
            )

        # Se intenta convertir la duración a número decimal.
        try:
            duracion_convertida = float(duracion)

        except (TypeError, ValueError) as error_original:
            raise DuracionInvalidaError(
                "La duración debe ser un valor numérico."
            ) from error_original

        # Se valida que la duración sea positiva.
        if duracion_convertida <= 0:
            raise DuracionInvalidaError(
                "La duración debe ser mayor que cero."
            )

        # Se almacenan las relaciones y los datos.
        self._codigo = str(codigo).strip()
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion_convertida
        self._estado = EstadoReserva.PENDIENTE
        self._costo_total = None

        # Se registra la creación de la reserva.
        registrar_evento(
            f"Reserva creada: {self._codigo}"
        )

    @property
    def codigo(self):
        """Devuelve el código de la reserva."""

        return self._codigo

    @property
    def cliente(self):
        """Devuelve el cliente asociado."""

        return self._cliente

    @property
    def servicio(self):
        """Devuelve el servicio reservado."""

        return self._servicio

    @property
    def duracion(self):
        """Devuelve la duración de la reserva."""

        return self._duracion

    @property
    def estado(self):
        """Devuelve el estado actual de la reserva."""

        return self._estado

    @property
    def costo_total(self):
        """Devuelve el costo total calculado."""

        return self._costo_total

    def confirmar(self):
        """
        Confirma una reserva pendiente.
        """

        if self._estado != EstadoReserva.PENDIENTE:
            raise EstadoReservaError(
                "Solo se pueden confirmar reservas pendientes."
            )

        try:
            self._servicio.validar_disponibilidad()

        except ServicioNoDisponibleError as error_original:
            raise ServicioNoDisponibleError(
                f"No fue posible confirmar la reserva {self._codigo}."
            ) from error_original

        self._estado = EstadoReserva.CONFIRMADA

        registrar_evento(
            f"Reserva confirmada: {self._codigo}"
        )

    def procesar(self, impuesto=0, descuento=0):
        """
        Procesa una reserva confirmada y calcula su costo.
        """

        if self._estado != EstadoReserva.CONFIRMADA:
            raise EstadoReservaError(
                "La reserva debe estar confirmada antes de procesarse."
            )

        self._costo_total = self._servicio.calcular_costo(
            self._duracion,
            impuesto,
            descuento
        )

        self._estado = EstadoReserva.PROCESADA

        registrar_evento(
            f"Reserva procesada: {self._codigo} | "
            f"Costo: {self._costo_total}"
        )

        return self._costo_total

    def cancelar(self, motivo="Sin motivo especificado"):
        """
        Cancela una reserva pendiente o confirmada.
        """

        if self._estado == EstadoReserva.PROCESADA:
            raise EstadoReservaError(
                "No se puede cancelar una reserva procesada."
            )

        if self._estado == EstadoReserva.CANCELADA:
            raise EstadoReservaError(
                "La reserva ya está cancelada."
            )

        if motivo is None or not str(motivo).strip():
            raise EstadoReservaError(
                "Debe indicarse un motivo de cancelación."
            )

        self._estado = EstadoReserva.CANCELADA

        registrar_evento(
            f"Reserva cancelada: {self._codigo} | "
            f"Motivo: {motivo}"
        )

    def obtener_informacion(self):
        """
        Devuelve la información completa de la reserva.
        """

        costo = (
            f"${self._costo_total:,.2f}"
            if self._costo_total is not None
            else "Pendiente"
        )

        return (
            f"Reserva: {self._codigo} | "
            f"Cliente: {self._cliente.nombre} | "
            f"Servicio: {self._servicio.nombre} | "
            f"Duración: {self._duracion} | "
            f"Estado: {self._estado.value} | "
            f"Costo: {costo}"
        )
