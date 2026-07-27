"""
Archivo: servicios.py

Este módulo contiene la clase abstracta Servicio y las clases
especializadas que representan los servicios ofrecidos por Software FJ.
"""

# Se importan ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod

# Se importa la clase abstracta general del sistema.
from entidad import EntidadSistema

# Se importan las excepciones relacionadas con servicios.
from excepciones import (
    TarifaInvalidaError,
    ParametroServicioError,
    ServicioNoDisponibleError,
    CalculoCostoError
)

# Se importa la función para registrar eventos.
from configuracion_log import registrar_evento


# Se define la clase abstracta Servicio.
class Servicio(EntidadSistema, ABC):
    """
    Representa un servicio general ofrecido por Software FJ.
    """

    # Se define el constructor de la clase.
    def __init__(self, codigo, nombre, tarifa_base, disponible=True):
        """
        Inicializa la información común de cualquier servicio.
        """

        # Se llama al constructor de la clase padre.
        super().__init__(codigo)

        # Se valida que el código no sea nulo.
        if codigo is None:
            raise ParametroServicioError(
                "El código del servicio no puede ser nulo."
            )

        # Se convierte el código a texto y se eliminan espacios.
        codigo_limpio = str(codigo).strip()

        # Se valida que el código no esté vacío.
        if not codigo_limpio:
            raise ParametroServicioError(
                "El código del servicio no puede estar vacío."
            )

        # Se valida que el nombre no sea nulo.
        if nombre is None:
            raise ParametroServicioError(
                "El nombre del servicio no puede ser nulo."
            )

        # Se convierte el nombre a texto y se eliminan espacios.
        nombre_limpio = str(nombre).strip()

        # Se valida que el nombre no esté vacío.
        if not nombre_limpio:
            raise ParametroServicioError(
                "El nombre del servicio no puede estar vacío."
            )

        # Se intenta convertir la tarifa a un número decimal.
        try:
            tarifa_convertida = float(tarifa_base)

        # Se capturan errores de tipo o conversión.
        except (TypeError, ValueError) as error_original:

            # Se lanza una excepción personalizada encadenada.
            raise TarifaInvalidaError(
                "La tarifa base debe ser un valor numérico."
            ) from error_original

        # Se valida que la tarifa sea mayor que cero.
        if tarifa_convertida <= 0:
            raise TarifaInvalidaError(
                "La tarifa base debe ser mayor que cero."
            )

        # Se almacenan los atributos protegidos.
        self._codigo = codigo_limpio
        self._nombre = nombre_limpio
        self._tarifa_base = tarifa_convertida
        self._disponible = bool(disponible)

        # Se registra la creación del servicio.
        registrar_evento(
            f"Servicio creado: {self._codigo} - {self._nombre}"
        )

    # Se crea una propiedad para consultar el código.
    @property
    def codigo(self):
        """Devuelve el código del servicio."""

        return self._codigo

    # Se crea una propiedad para consultar el nombre.
    @property
    def nombre(self):
        """Devuelve el nombre del servicio."""

        return self._nombre

    # Se crea una propiedad para consultar la tarifa base.
    @property
    def tarifa_base(self):
        """Devuelve la tarifa base del servicio."""

        return self._tarifa_base

    # Se crea una propiedad para consultar la disponibilidad.
    @property
    def disponible(self):
        """Indica si el servicio está disponible."""

        return self._disponible

    # Se define un método para cambiar la disponibilidad.
    def cambiar_disponibilidad(self, disponible):
        """
        Actualiza el estado de disponibilidad del servicio.
        """

        # Se convierte el valor recibido a booleano.
        self._disponible = bool(disponible)

        # Se registra el cambio en el archivo de logs.
        registrar_evento(
            f"Disponibilidad del servicio {self._codigo}: "
            f"{self._disponible}"
        )

    # Se define un método para validar la disponibilidad.
    def validar_disponibilidad(self):
        """
        Comprueba que el servicio esté disponible.
        """

        # Se verifica si el servicio no está disponible.
        if not self._disponible:
            raise ServicioNoDisponibleError(
                f"El servicio {self._nombre} no está disponible."
            )

        # Se retorna True cuando está disponible.
        return True

    # Se crea un método auxiliar para aplicar impuesto y descuento.
    def _aplicar_ajustes(self, subtotal, impuesto=0, descuento=0):
        """
        Aplica impuesto y descuento al subtotal calculado.
        """

        try:
            impuesto_convertido = float(impuesto)
            descuento_convertido = float(descuento)

        except (TypeError, ValueError) as error_original:
            raise CalculoCostoError(
                "El impuesto y el descuento deben ser numéricos."
            ) from error_original

        if impuesto_convertido < 0 or impuesto_convertido > 100:
            raise CalculoCostoError(
                "El impuesto debe estar entre 0 y 100."
            )

        if descuento_convertido < 0 or descuento_convertido > 100:
            raise CalculoCostoError(
                "El descuento debe estar entre 0 y 100."
            )

        subtotal_con_descuento = subtotal * (
            1 - descuento_convertido / 100
        )

        total = subtotal_con_descuento * (
            1 + impuesto_convertido / 100
        )

        return round(total, 2)

    # Se define el método abstracto para calcular costos.
    @abstractmethod
    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo total del servicio.
        """

        raise NotImplementedError

    # Se define el método abstracto para validar parámetros.
    @abstractmethod
    def validar_parametros(self):
        """
        Valida los parámetros particulares de cada servicio.
        """

        raise NotImplementedError

    # Se define el método abstracto para describir el servicio.
    @abstractmethod
    def describir_servicio(self):
        """
        Devuelve una descripción del servicio.
        """

        raise NotImplementedError

    # Se implementa el método heredado de EntidadSistema.
    def obtener_informacion(self):
        """
        Devuelve la información general del servicio.
        """

        return (
            f"Código: {self._codigo} | "
            f"Servicio: {self._nombre} | "
            f"Tarifa base: ${self._tarifa_base:,.2f} | "
            f"Disponible: {'Sí' if self._disponible else 'No'}"
        )


# Se crea la clase especializada ReservaSala.
class ReservaSala(Servicio):
    """
    Representa el servicio de reserva de una sala.
    """

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_base,
        capacidad,
        incluye_proyector=False,
        disponible=True
    ):
        """
        Inicializa una sala disponible para reservas.
        """

        super().__init__(
            codigo,
            nombre,
            tarifa_base,
            disponible
        )

        self.capacidad = capacidad
        self.incluye_proyector = bool(incluye_proyector)

        self.validar_parametros()

    def validar_parametros(self):
        """
        Valida la capacidad de la sala.
        """

        if not isinstance(self.capacidad, int):
            raise ParametroServicioError(
                "La capacidad de la sala debe ser un número entero."
            )

        if self.capacidad <= 0:
            raise ParametroServicioError(
                "La capacidad de la sala debe ser mayor que cero."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo por horas de uso de la sala.
        """

        try:
            duracion_convertida = float(duracion)

        except (TypeError, ValueError) as error_original:
            raise CalculoCostoError(
                "La duración de la sala debe ser numérica."
            ) from error_original

        if duracion_convertida <= 0:
            raise CalculoCostoError(
                "La duración debe ser mayor que cero."
            )

        subtotal = self._tarifa_base * duracion_convertida

        if self.incluye_proyector:
            subtotal += 15000 * duracion_convertida

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def describir_servicio(self):
        """
        Devuelve la descripción específica de la sala.
        """

        proyector = "Sí" if self.incluye_proyector else "No"

        return (
            f"Sala con capacidad para {self.capacidad} personas. "
            f"Incluye proyector: {proyector}."
        )


# Se crea la clase especializada AlquilerEquipo.
class AlquilerEquipo(Servicio):
    """
    Representa el alquiler temporal de un equipo.
    """

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_base,
        tipo_equipo,
        deposito_garantia=0,
        disponible=True
    ):
        """
        Inicializa un equipo disponible para alquiler.
        """

        super().__init__(
            codigo,
            nombre,
            tarifa_base,
            disponible
        )

        self.tipo_equipo = tipo_equipo

        try:
            self.deposito_garantia = float(deposito_garantia)

        except (TypeError, ValueError) as error_original:
            raise ParametroServicioError(
                "El depósito debe ser un valor numérico."
            ) from error_original

        self.validar_parametros()

    def validar_parametros(self):
        """
        Valida el tipo de equipo y el depósito.
        """

        if self.tipo_equipo is None:
            raise ParametroServicioError(
                "El tipo de equipo no puede ser nulo."
            )

        if not str(self.tipo_equipo).strip():
            raise ParametroServicioError(
                "El tipo de equipo no puede estar vacío."
            )

        self.tipo_equipo = str(self.tipo_equipo).strip()

        if self.deposito_garantia < 0:
            raise ParametroServicioError(
                "El depósito no puede ser negativo."
            )

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo por días de alquiler.
        """

        try:
            duracion_convertida = float(duracion)

        except (TypeError, ValueError) as error_original:
            raise CalculoCostoError(
                "La duración del alquiler debe ser numérica."
            ) from error_original

        if duracion_convertida <= 0:
            raise CalculoCostoError(
                "La duración debe ser mayor que cero."
            )

        subtotal = (
            self._tarifa_base * duracion_convertida
            + self.deposito_garantia
        )

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def describir_servicio(self):
        """
        Devuelve la descripción del equipo.
        """

        return (
            f"Alquiler de {self.tipo_equipo}. "
            f"Depósito de garantía: "
            f"${self.deposito_garantia:,.2f}."
        )


# Se crea la clase especializada AsesoriaEspecializada.
class AsesoriaEspecializada(Servicio):
    """
    Representa una asesoría profesional especializada.
    """

    def __init__(
        self,
        codigo,
        nombre,
        tarifa_base,
        especialidad,
        nivel_experto=False,
        disponible=True
    ):
        """
        Inicializa una asesoría especializada.
        """

        super().__init__(
            codigo,
            nombre,
            tarifa_base,
            disponible
        )

        self.especialidad = especialidad
        self.nivel_experto = bool(nivel_experto)

        self.validar_parametros()

    def validar_parametros(self):
        """
        Valida la especialidad de la asesoría.
        """

        if self.especialidad is None:
            raise ParametroServicioError(
                "La especialidad no puede ser nula."
            )

        if not str(self.especialidad).strip():
            raise ParametroServicioError(
                "La especialidad no puede estar vacía."
            )

        self.especialidad = str(self.especialidad).strip()

        return True

    def calcular_costo(self, duracion, impuesto=0, descuento=0):
        """
        Calcula el costo por horas de asesoría.
        """

        try:
            duracion_convertida = float(duracion)

        except (TypeError, ValueError) as error_original:
            raise CalculoCostoError(
                "La duración de la asesoría debe ser numérica."
            ) from error_original

        if duracion_convertida <= 0:
            raise CalculoCostoError(
                "La duración debe ser mayor que cero."
            )

        subtotal = self._tarifa_base * duracion_convertida

        if self.nivel_experto:
            subtotal *= 1.25

        return self._aplicar_ajustes(
            subtotal,
            impuesto,
            descuento
        )

    def describir_servicio(self):
        """
        Devuelve la descripción de la asesoría.
        """

        nivel = "experto" if self.nivel_experto else "estándar"

        return (
            f"Asesoría en {self.especialidad}. "
            f"Nivel profesional: {nivel}."
        )
