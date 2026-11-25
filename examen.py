from funciones import (
    cargar_juegos_csv,
    dar_de_alta_juego,
    registrar_venta,
    mostrar_estadisticas,
    mostrar_catalogo_ordenado,
)

RUTA_CSV = "juegos.csv"

def mostrar_menu() -> None:
    """
    Muestra el menu principal del sistema en consola
    """
    print("=== SISTEMA DE GESTION DE VIDEOJUEGOS ===")
    print("1. Alta de videojuego")
    print("2. Registrar una venta")
    print("3. Consultar estadisticas")
    print("4. Mostrar catalogo ordenado")
    print("5. Salir")


def main() -> None:
    """
    Funcion principal que inicializa el catalogo y ejecuta el bucle del menu
    """
    catalogo = cargar_juegos_csv(RUTA_CSV)

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion (1-5): ")

        if opcion == "1":
            dar_de_alta_juego(catalogo, RUTA_CSV)
        elif opcion == "2":
            registrar_venta(catalogo, RUTA_CSV)
        elif opcion == "3":
            mostrar_estadisticas(catalogo)
        elif opcion == "4":
            mostrar_catalogo_ordenado(catalogo)
        elif opcion == "5":
            print("Programa finalizado.")
            break
        else:
            print("Opcion invalida. Ingrese un numero del 1 al 5")

main()