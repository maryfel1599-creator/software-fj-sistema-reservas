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

# Se crea una excepción general para errores de servicios.
class ErrorServicio(ErrorSistemaFJ):
    """Se genera cuando ocurre un error relacionado con un servicio."""

    pass

# Se crea una excepción para servicios que no se encuentran disponibles.
class ServicioNoDisponibleError(ErrorServicio):
    """Se genera cuando se intenta reservar un servicio no disponible."""

    pass

# Se crea una excepción para tarifas inválidas.
class TarifaInvalidaError(ErrorServicio):
    """Se genera cuando una tarifa es igual o menor que cero."""

    pass

# Se crea una excepción para parámetros incorrectos de los servicios.
class ParametroServicioError(ErrorServicio):
    """Se genera cuando un servicio recibe parámetros inválidos."""

    pass

# Se crea una excepción general para errores de reservas.
class ErrorReserva(ErrorSistemaFJ):
    """Se genera cuando ocurre un problema con una reserva."""

    pass

# Se crea una excepción para duraciones incorrectas.
class DuracionInvalidaError(ErrorReserva):
    """Se genera cuando la duración de la reserva es inválida."""

    pass

# Se crea una excepción para estados no permitidos.
class EstadoReservaError(ErrorReserva):
    """Se genera cuando una operación no corresponde al estado de la reserva."""

    pass

# Se crea una excepción para reservas que no existen.
class ReservaNoEncontradaError(ErrorReserva):
    """Se genera cuando no se encuentra una reserva solicitada."""

    pass

# Se crea una excepción para clientes que no existen.
class ClienteNoEncontradoError(ErrorCliente):
    """Se genera cuando no se encuentra un cliente solicitado."""

    pass

# Se crea una excepción para servicios que no existen.
class ServicioNoEncontradoError(ErrorServicio):
    """Se genera cuando no se encuentra un servicio solicitado."""

    pass
