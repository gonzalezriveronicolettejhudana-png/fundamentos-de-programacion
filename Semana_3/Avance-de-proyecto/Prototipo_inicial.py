# Prototipo inicial para registrar ventas de una sucursal de LECAROZ # Proyecto escolar: los productos y precios son ejemplos, no precios oficiales.

def mostrar_productos(productos):
    print("\n--- PRODUCTOS ---")
    for numero, (nombre, precio) in enumerate(productos.items(), start=1):
        print(f"{numero}. {nombre}: ${precio:.2f}")


def registrar_venta(productos):
    nombres = list(productos.keys())
    cantidades = {}
    total_compra = 0.0

    print("\nVoy a registrar una venta.")
    mostrar_productos(productos)

    for nombre in nombres:
        while True:
            entrada = input(
                f"¿Cuántas piezas de {nombre} se vendieron? "
            )

            try:
                cantidad = int(entrada)

                if cantidad < 0:
                    print(
                        "La cantidad no puede ser negativa. "
                        "Intenta otra vez."
                    )
                    continue

                cantidades[nombre] = cantidad
                break

            except ValueError:
                print("Escribe un número entero, por favor.")

    print("\n--- TICKET DE VENTA ---")
    hay_productos = False

    for nombre, cantidad in cantidades.items():
        if cantidad > 0:
            importe = productos[nombre] * cantidad
            total_compra += importe
            hay_productos = True

            print(
                f"{nombre}: {cantidad} x "
                f"${productos[nombre]:.2f} = ${importe:.2f}"
            )

    if not hay_productos:
        print(
            "No se registró la venta porque "
            "no se eligieron productos."
        )
        return 0.0, False

    print(f"Total a pagar: ${total_compra:.2f}")
    return total_compra, True


def main():
    # Precios ficticios para el ejercicio.
    # Deben actualizarse con datos autorizados si fuera necesario.
    productos = {
        "Concha": 15.00,
        "Bolillo": 4.00,
        "Dona": 18.00,
        "Oreja": 16.00,
        "Rebanada de pastel": 45.00,
    }

    total_dia = 0.0
    contador_ventas = 0
    opcion = ""

    while opcion != "3":
        print("\n===== LECAROZ: REGISTRO DE VENTAS =====")
        print("1. Registrar una venta")
        print("2. Consultar resumen del día")
        print("3. Salir")

        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            total, venta_valida = registrar_venta(productos)

            if venta_valida:
                total_dia += total
                contador_ventas += 1
                print("La venta se registró correctamente.")

        elif opcion == "2":
            print("\n--- RESUMEN DEL DÍA ---")
            print(f"Ventas registradas: {contador_ventas}")
            print(f"Total vendido: ${total_dia:.2f}")

        elif opcion == "3":
            print("\nCerrando el programa.")
            print(f"Ventas registradas: {contador_ventas}")
            print(
                "Total vendido durante esta sesión: "
                f"${total_dia:.2f}"
            )

        else:
            print("Opción no válida. Elige 1, 2 o 3.")


if __name__ == "__main__":
    main()
