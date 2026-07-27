"""
Archivo: entidad.py

Este módulo contiene la clase abstracta EntidadSistema.

Todas las entidades del sistema heredarán de esta clase,
garantizando una estructura común para el proyecto.
"""

# Se importan ABC y abstractmethod para crear clases abstractas.
from abc import ABC, abstractmethod


# Se define una clase abstracta llamada EntidadSistema.
class EntidadSistema(ABC):
    """
    Clase abstracta que representa una entidad general
    dentro del Sistema Software FJ.
    """

    # Se define el constructor de la clase.
    def __init__(self, identificador):
        """
        Inicializa una entidad con un identificador.

        Args:
            identificador: Código o documento que identifica la entidad.
        """

        # Se valida que el identificador no sea nulo.
        if identificador is None:
            raise ValueError("El identificador no puede ser nulo.")

        # Se convierte el identificador a texto y se eliminan espacios.
        identificador_limpio = str(identificador).strip()

        # Se valida que el identificador no esté vacío.
        if not identificador_limpio:
            raise ValueError("El identificador no puede estar vacío.")

        # Se almacena el identificador como atributo protegido.
        self._identificador = identificador_limpio

    # Se crea una propiedad que devuelve el identificador.
    @property
    def identificador(self):
        """
        Devuelve el identificador de la entidad.
        """

        return self._identificador

    # Se define un método abstracto para obtener información.
    @abstractmethod
    def obtener_informacion(self):
        """
        Devuelve la información principal de la entidad.
        """

        raise NotImplementedError(
            "Las clases derivadas deben implementar obtener_informacion()."
        )

    # Se sobrescribe el método especial __str__.
    def __str__(self):
        """
        Devuelve una representación legible de la entidad.
        """

        return self.obtener_informacion()
