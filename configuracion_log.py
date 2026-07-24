"""
Archivo: configuracion_log.py

Este módulo configura el sistema de registros de eventos y errores
del Sistema Integral de Gestión de Software FJ.
"""
#Se importa el módulo logging para registrar eventos y errores.
import logging

#Se importa os para gestionar rutas y crear carpetas.
import os

# Se define el nombre de la carpeta donde se almacenarán los logs.
CARPETA_LOGS = "logs"

# Se verifica si la carpeta de logs existe.
if not os.path.exists(CARPETA_LOGS):

    # Si la carpeta no existe, se crea automáticamente.
    os.makedirs(CARPETA_LOGS)

# Se construye la ruta completa del archivo de registro.
RUTA_LOG = os.path.join(CARPETA_LOGS, "software_fj.log")

# Se configura el comportamiento general del sistema de logs.
logging.basicConfig(

    # Se indica el archivo donde se almacenarán los registros.
    filename=RUTA_LOG,

    # Se establece el nivel mínimo de registro.
    level=logging.INFO,

    # Se define el formato de cada línea del archivo de logs.
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",

    # Se establece la codificación para admitir caracteres especiales.
    encoding="utf-8"

  # Se crea un logger específico para el sistema Software FJ.
logger = logging.getLogger("SoftwareFJ")

# Esta función registra eventos normales del sistema.
def registrar_evento(mensaje):
    """
    Registra un evento informativo en el archivo de logs.
    """

    # El mensaje se guarda con nivel INFO.
    logger.info(mensaje)

# Esta función registra advertencias.
def registrar_advertencia(mensaje):
    """
    Registra una advertencia en el archivo de logs.
    """

    # El mensaje se guarda con nivel WARNING.
    logger.warning(mensaje)

# Esta función registra errores controlados.
def registrar_error(mensaje):
    """
    Registra un error en el archivo de logs.
    """

    # El mensaje se guarda con nivel ERROR.
    logger.error(mensaje)

# Esta función registra errores junto con su traza técnica.
def registrar_excepcion(mensaje):
    """
    Registra una excepción y su seguimiento técnico.
    """

    # El método exception guarda el mensaje y la traza del error.
    logger.exception(mensaje)
