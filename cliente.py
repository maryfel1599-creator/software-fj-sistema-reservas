"""
Archivo: cliente.py

Este módulo contiene la clase Cliente.

La clase administra los datos personales de los clientes
registrados en el Sistema Integral de Gestión de Software FJ.
"""
# Se importa el módulo re para validar correos electrónicos.
import re

# Se importa la clase abstracta EntidadSistema.
from entidad import EntidadSistema

# Se importan las excepciones relacionadas con clientes.
from excepciones import (
    DocumentoInvalidoError,
    NombreInvalidoError,
    CorreoInvalidoError,
    TelefonoInvalidoError
)

# Se importa la función para registrar eventos.
from configuracion_log import registrar_evento

# Se define la clase Cliente.
class Cliente(EntidadSistema):
    """
    Representa un cliente registrado en Software FJ.
    """

# Se define el constructor de la clase.
    def __init__(self, documento, nombre, correo, telefono):

    # Se llama al constructor de la clase padre.
        super().__init__(documento)  

# Se inicializan los atributos privados.
        self.__documento = None
        self.__nombre = None
        self.__correo = None
        self.__telefono = None

   # Se asignan los datos mediante las propiedades.
        # Esto permite ejecutar las validaciones de cada setter.
        self.documento = documento
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono

  # Se registra en el archivo de logs la creación del cliente.
        registrar_evento(
            f"Cliente creado correctamente: {self.__documento}"
        )

   # Se crea la propiedad documento.
    @property
    def documento(self):
        """
        Devuelve el documento del cliente.
        """

  return self.__documento

 # Se crea el método setter para validar y asignar el documento.
    @documento.setter
    def documento(self, valor):
        """
        Valida y asigna el documento del cliente.
        """

# Se comprueba que el valor no sea nulo.
        if valor is None:
            raise DocumentoInvalidoError(
                "El documento no puede ser nulo."
            )

        # Se convierte el valor a texto y se eliminan espacios.
        documento_limpio = str(valor).strip()

# Se comprueba que el documento no esté vacío.
        if not documento_limpio:
            raise DocumentoInvalidoError(
                "El documento no puede estar vacío."
            )

      # Se comprueba que contenga únicamente números.
        if not documento_limpio.isdigit():
            raise DocumentoInvalidoError(
                "El documento solo puede contener números."

         # Se comprueba que tenga una longitud mínima.
        if len(documento_limpio) < 5:
            raise DocumentoInvalidoError(
                "El documento debe tener al menos cinco dígitos."
            )

        # Se almacena el documento validado.
        self.__documento = documento_limpio
      
