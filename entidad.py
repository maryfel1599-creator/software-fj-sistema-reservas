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

# Constructor de la clase.
    def __init__(self, identificador):

        # Se almacena el identificador como atributo protegido.
        self._identificador = identificador

   # Propiedad que devuelve el identificador.
    @property
    def identificador(self):
        """
        Devuelve el identificador de la entidad.
        """

        return self._identificador

  # Método abstracto que todas las clases hijas deberán implementar.
    @abstractmethod
    def obtener_informacion(self):
        """
        Devuelve la información principal
        de la entidad.
        """

        pass
