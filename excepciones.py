"""
Archivo: excepciones.py
Este módulo contiene las excepeciones personalizadas utilizadas 
por el Sistema Integral de Gestión de Software FJ. 
"""
# Se crea una excepción general para todos los errores del sistema.
class ErrorSistemaFJ(Exception):
    """Clase base para las excepciones personalizadas del sistema."""

    # No requiere código adicional porque hereda de Exception.
    pass
#Se crea una excepción para errores relacionados con clientes. 
class ErrorCliente(ErrorSistemaFJ):
    """Se genera cuadno los datos de un cliente son inválidos."""

pass

#Se crea uan excepción específica para documentos incorrectos.
class DocumentoIvalidoError(ErrorCliente):
    """Se genera cuando el documento del cliente no es válido."""

pass

#Se crea una exepción para nombres inválidos.
class NombreIvalidoError(ErrorCliente):
    """Se genera cuando el nombre del cliente está cacío o es incorrecto."""

pass

#Se crea una excepción para correos electrónicos inválidos.
class CorreoInvalidoError(ErrorCliente):
    """Se genera cuando el correo electrónico no cumple el formato esperado."""

pass

# Se crea una excepción para teléfonos inválidos.
class TelefonoInvalidoError(ErrorCliente):
    """Se genera cuando el teléfono contiene datos incorrectos."""

    pass
