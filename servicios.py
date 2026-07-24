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
    ServicioNoDisponibleError
)


# Se importa la función para registrar eventos.
from configuracion_log import registrar_evento

# Se define la clase abstracta Servicio.
class Servicio(EntidadSistema, ABC):
    """
    Representa un servicio general ofrecido por Software FJ.

    Esta clase no puede ser instanciada directamente, porque contiene
    métodos abstractos que deben ser implementados por las clases hijas.
    """

    # Se define el constructor de la clase.
    def __init__(self, codigo, nombre, tarifa_base, disponible=True):

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

        # Se capturan errores de tipo o de conversión.
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
        """
        Devuelve el código del servicio.
        """

        return self._codigo

    # Se crea una propiedad para consultar el nombre.
    @property
    def nombre(self):
        """
        Devuelve el nombre del servicio.
        """

        return self._nombre

    # Se crea una propiedad para consultar la tarifa base.
    @property
    def tarifa_base(self):
        """
        Devuelve la tarifa base del servicio.
        """

        return self._tarifa_base

    # Se crea una propiedad para consultar la disponibilidad.
    @property
    def disponible(self):
        """
        Indica si el servicio está disponible.
        """

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

  # Se define el método abstracto para calcular costos.
    @abstractmethod
    def calcular_costo(
        self,
        duracion,
        impuesto=0,
        descuento=0
    ):
        """
        Calcula el costo total del servicio.
        """

        pass

    # Se define el método abstracto para validar parámetros.
    @abstractmethod
    def validar_parametros(self):
        """
        Valida los parámetros particulares de cada servicio.
        """

        pass

    # Se define el método abstracto para describir el servicio.
    @abstractmethod
    def describir_servicio(self):
        """
        Devuelve una descripción del servicio.
        """

        pass

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
