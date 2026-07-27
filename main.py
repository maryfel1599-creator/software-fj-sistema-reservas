"""
Archivo: main.py

Este archivo ejecuta una simulación completa con operaciones
válidas e inválidas para demostrar la estabilidad del sistema.
"""

# Se importan las clases del proyecto.
from cliente import Cliente

from servicios import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from gestor_sistema import GestorSistema

# Se importa la excepción general del sistema.
from excepciones import ErrorSistemaFJ

# Se importan funciones de registro.
from configuracion_log import (
    registrar_evento,
    registrar_excepcion
)


# Se define una función para ejecutar cada operación.
def ejecutar_operacion(numero, descripcion, funcion):
    """
    Ejecuta una operación y controla sus posibles errores.

    Esta función demuestra el uso de:
    try/except, try/except/else y try/except/finally.
    """

    print()
    print(f"OPERACIÓN {numero}: {descripcion}")

    try:
        # Se ejecuta la función recibida.
        resultado = funcion()

    except ErrorSistemaFJ as error:
        # Se capturan las excepciones propias del proyecto.
        registrar_excepcion(
            f"Error controlado en la operación {numero}: {error}"
        )

        print(f"Resultado: ERROR CONTROLADO - {error}")

    except (TypeError, ValueError) as error:
        # Se capturan errores comunes de Python.
        registrar_excepcion(
            f"Error de datos en la operación {numero}: {error}"
        )

        print(f"Resultado: ERROR DE DATOS - {error}")

    except Exception as error:
        # Se capturan errores inesperados para evitar que el sistema finalice.
        registrar_excepcion(
            f"Error inesperado en la operación {numero}: {error}"
        )

        print(f"Resultado: ERROR INESPERADO - {error}")

    else:
        # Este bloque solo se ejecuta cuando no existe ninguna excepción.
        registrar_evento(
            f"Operación {numero} ejecutada correctamente."
        )

        if resultado is not None:
            print(resultado)

        print("Resultado: OPERACIÓN EXITOSA")

    finally:
        # Este bloque siempre se ejecuta.
        print("Estado: La aplicación continúa funcionando.")


# Se define la función principal.
def main():
    """
    Ejecuta al menos diez operaciones completas del sistema.
    """

    # Se crea el gestor que almacenará los objetos en memoria.
    gestor = GestorSistema()

    # Operación 1: cliente correcto.
    ejecutar_operacion(
        1,
        "Registrar un cliente válido",
        lambda: gestor.registrar_cliente(
            Cliente(
                "1098765432",
                "Ana Martínez",
                "ana@correo.com",
                "3001234567"
            )
        )
    )

    # Operación 2: correo incorrecto.
    ejecutar_operacion(
        2,
        "Registrar cliente con correo inválido",
        lambda: gestor.registrar_cliente(
            Cliente(
                "1098765433",
                "Carlos Pérez",
                "correo-invalido",
                "3011234567"
            )
        )
    )

    # Operación 3: segundo cliente correcto.
    ejecutar_operacion(
        3,
        "Registrar un segundo cliente válido",
        lambda: gestor.registrar_cliente(
            Cliente(
                "1098765434",
                "Laura Gómez",
                "laura@correo.com",
                "3021234567"
            )
        )
    )

    # Operación 4: cliente duplicado.
    ejecutar_operacion(
        4,
        "Intentar registrar un cliente duplicado",
        lambda: gestor.registrar_cliente(
            Cliente(
                "1098765432",
                "Persona Repetida",
                "repetida@correo.com",
                "3031234567"
            )
        )
    )

    # Operación 5: sala correcta.
    ejecutar_operacion(
        5,
        "Registrar servicio de reserva de sala",
        lambda: gestor.registrar_servicio(
            ReservaSala(
                "SER-001",
                "Sala Ejecutiva",
                50000,
                capacidad=12,
                incluye_proyector=True
            )
        )
    )

    # Operación 6: equipo correcto.
    ejecutar_operacion(
        6,
        "Registrar servicio de alquiler de equipo",
        lambda: gestor.registrar_servicio(
            AlquilerEquipo(
                "SER-002",
                "Alquiler de portátil",
                80000,
                tipo_equipo="Computador portátil",
                deposito_garantia=100000
            )
        )
    )

    # Operación 7: asesoría no disponible.
    ejecutar_operacion(
        7,
        "Registrar asesoría especializada no disponible",
        lambda: gestor.registrar_servicio(
            AsesoriaEspecializada(
                "SER-003",
                "Asesoría de ciberseguridad",
                120000,
                especialidad="Ciberseguridad",
                nivel_experto=True,
                disponible=False
            )
        )
    )

    # Operación 8: tarifa inválida.
    ejecutar_operacion(
        8,
        "Registrar servicio con tarifa negativa",
        lambda: gestor.registrar_servicio(
            ReservaSala(
                "SER-004",
                "Sala incorrecta",
                -5000,
                capacidad=5
            )
        )
    )

    # Operación 9: reserva correcta.
    ejecutar_operacion(
        9,
        "Crear una reserva válida",
        lambda: gestor.crear_reserva(
            "RES-001",
            "1098765432",
            "SER-001",
            2
        ).obtener_informacion()
    )

    # Operación 10: confirmar reserva.
    ejecutar_operacion(
        10,
        "Confirmar la reserva válida",
        lambda: (
            gestor.buscar_reserva("RES-001").confirmar(),
            gestor.buscar_reserva("RES-001").obtener_informacion()
        )[1]
    )

    # Operación 11: procesar con impuesto y descuento.
    ejecutar_operacion(
        11,
        "Procesar reserva con impuesto y descuento",
        lambda: (
            gestor.buscar_reserva("RES-001").procesar(
                impuesto=19,
                descuento=10
            ),
            gestor.buscar_reserva("RES-001").obtener_informacion()
        )[1]
    )

    # Operación 12: cancelar una reserva procesada.
    ejecutar_operacion(
        12,
        "Intentar cancelar una reserva procesada",
        lambda: gestor.buscar_reserva("RES-001").cancelar(
            "Cambio de decisión del cliente."
        )
    )

    # Operación 13: duración inválida.
    ejecutar_operacion(
        13,
        "Crear reserva con duración negativa",
        lambda: gestor.crear_reserva(
            "RES-002",
            "1098765434",
            "SER-002",
            -2
        )
    )

    # Operación 14: cliente inexistente.
    ejecutar_operacion(
        14,
        "Crear reserva con cliente inexistente",
        lambda: gestor.crear_reserva(
            "RES-003",
            "9999999999",
            "SER-002",
            1
        )
    )

    # Operación 15: servicio no disponible.
    ejecutar_operacion(
        15,
        "Confirmar una reserva de servicio no disponible",
        lambda: (
            gestor.crear_reserva(
                "RES-004",
                "1098765434",
                "SER-003",
                2
            ).confirmar()
        )
    )

    # Operación 16: cálculo inválido.
    ejecutar_operacion(
        16,
        "Calcular costo con impuesto incorrecto",
        lambda: gestor.buscar_servicio(
            "SER-001"
        ).calcular_costo(
            1,
            impuesto=150
        )
    )

    # Operación 17: polimorfismo.
    ejecutar_operacion(
        17,
        "Mostrar descripciones polimórficas",
        lambda: "\n".join(
            servicio.describir_servicio()
            for servicio in gestor.listar_servicios()
        )
    )

    # Operación 18: resumen final.
    ejecutar_operacion(
        18,
        "Mostrar resumen general",
        gestor.obtener_resumen
    )


# Se verifica que el archivo sea ejecutado directamente.
if __name__ == "__main__":

    # Se llama a la función principal.
    main()
