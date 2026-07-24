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
      
# Se crea la propiedad nombre.
    @property
    def nombre(self):
        """
        Devuelve el nombre del cliente.
        """

return self.__nombre

# Se crea el método setter del nombre.
    @nombre.setter
    def nombre(self, valor):
        """
        Valida y asigna el nombre del cliente.
        """

 # Se comprueba que el nombre no sea nulo.
        if valor is None:
            raise NombreInvalidoError(
                "El nombre no puede ser nulo."
            )

 # Se convierte a texto y se eliminan espacios.
        nombre_limpio = str(valor).strip()

 # Se comprueba que el nombre no esté vacío.
        if not nombre_limpio:
            raise NombreInvalidoError(
                "El nombre no puede estar vacío."
            )

 # Se comprueba que tenga una longitud mínima.
        if len(nombre_limpio) < 3:
            raise NombreInvalidoError(
                "El nombre debe tener al menos tres caracteres."
            )

# Se comprueba que no esté formado únicamente por números.
        if nombre_limpio.isdigit():
            raise NombreInvalidoError(
                "El nombre no puede contener únicamente números."
            )

# Se almacena el nombre validado.
        self.__nombre = nombre_limpio

# Se crea la propiedad correo.
@property
def correo(self):
    """
    Devuelve el correo electrónico del cliente.
    """
    return self.__correo

# Se crea el método setter para validar y asignar el correo.
    @correo.setter
    def correo(self, valor):
        """
        Valida y asigna el correo electrónico del cliente.
        """

 # Se comprueba que el correo no sea nulo.
        if valor is None:
            raise CorreoInvalidoError(
                "El correo no puede ser nulo."
            )

# Se convierte el correo a texto, se eliminan espacios
        # y se transforma a minúsculas.
        correo_limpio = str(valor).strip().lower()

 # Se define una expresión regular para validar el correo.
        patron_correo = (
            r"^[A-Za-z0-9._%+-]+@"
            r"[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
        )

 # Se comprueba que el correo coincida con el patrón.
        if not re.match(patron_correo, correo_limpio):
            raise CorreoInvalidoError(
                "El correo electrónico no tiene un formato válido."
            )

 # Se almacena el correo validado.
        self.__correo = correo_limpio

# Se crea la propiedad teléfono.
    @property
    def telefono(self):
        """
        Devuelve el teléfono del cliente.
        """

return self.__telefono

# Se crea el método setter para validar y asignar el teléfono.
    @telefono.setter
    def telefono(self, valor):
        """
        Valida y asigna el teléfono del cliente.
        """

 # Se comprueba que el teléfono no sea nulo.
        if valor is None:
            raise TelefonoInvalidoError(
                "El teléfono no puede ser nulo."
            )

 # Se convierte el teléfono a texto y se eliminan espacios.
        telefono_limpio = str(valor).strip()

# Se comprueba que el teléfono no esté vacío.
        if not telefono_limpio:
            raise TelefonoInvalidoError(
                "El teléfono no puede estar vacío."
            )

 # Se comprueba que contenga únicamente números.
        if not telefono_limpio.isdigit():
            raise TelefonoInvalidoError(
                "El teléfono solo puede contener números."
            )

# Se comprueba que tenga entre 7 y 10 dígitos.
        if len(telefono_limpio) < 7 or len(telefono_limpio) > 10:
            raise TelefonoInvalidoError(
                "El teléfono debe tener entre 7 y 10 dígitos."
            )

  # Se almacena el teléfono validado.
        self.__telefono = telefono_limpio


         # Se sobrescribe el método abstracto de la clase padre.
    def obtener_informacion(self):
        """
        Devuelve la información completa del cliente.
        """

  # Se construye y retorna una cadena con los datos.
        return (
            f"Documento: {self.__documento} | "
            f"Nombre: {self.__nombre} | "
            f"Correo: {self.__correo} | "
            f"Teléfono: {self.__telefono}"
        )    
# Se sobrescribe el método especial __str__.
    def __str__(self):
        """
        Devuelve una representación legible del cliente.
        """

        # Se reutiliza el método obtener_informacion.
        return self.obtener_informacion()
