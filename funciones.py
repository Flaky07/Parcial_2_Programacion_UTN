import random

GENEROS_VALIDOS = ("RPG", "Deportes", "Carreras", "Aventura", "Estrategia")


def intercambiar_elementos(lista: list, i: int, j: int) -> None:
    """
    Intercambia dos elementos de posicion en una lista
    Parametros:
        lista: lista de elementos a modificar
        i: indice del primer elemento
        j: indice del segundo elemento
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista[j] = aux


def cargar_juegos_csv(ruta_archivo: str) -> list:
    """
    Carga los videojuegos desde un archivo CSV
    Parametros:
        ruta_archivo: ruta del archivo CSV a leer
    Retorna:
        Lista de diccionarios con los videojuegos cargados
    """
    catalogo = []

    try:
        with open(ruta_archivo, "r") as archivo:
            lineas = archivo.readlines()

        for indice in range(len(lineas)):
            linea = lineas[indice].strip()
            if linea == "":
                continue

            if indice == 0 and "codigo_identificador" in linea.lower():
                continue

            campos = linea.split(",")
            if len(campos) == 6:
                juego = {
                    "codigo_identificador": int(campos[0].strip()),
                    "nombre": campos[1].strip(),
                    "genero": campos[2].strip(),
                    "precio": float(campos[3].strip()),
                    "stock": int(campos[4].strip()),
                    "unidades_vendidas": int(campos[5].strip()),
                }
                catalogo.append(juego)
    except:
        print(f"Aviso: no se encontro el archivo '{ruta_archivo}'. Se inicia catalogo vacio.")

    return catalogo


def guardar_juegos_csv(ruta_archivo: str, catalogo: list) -> None:
    """
    Guarda el catalogo completo en un archivo CSV sin usar el modulo csv
    Parametros:
        ruta_archivo: ruta del archivo CSV a escribir
        catalogo: lista de diccionarios de videojuegos
    """
    with open(ruta_archivo, "w") as archivo:
        archivo.write("codigo_identificador,nombre,genero,precio,stock,unidades_vendidas")
        for juego in catalogo:
            linea = (
                f"{juego['codigo_identificador']},"
                f"{juego['nombre']},"
                f"{juego['genero']},"
                f"{juego['precio']},"
                f"{juego['stock']},"
                f"{juego['unidades_vendidas']}"
            )
            archivo.write(linea)


def generar_codigo_unico(catalogo: list) -> int:
    """
    Genera un codigo identificador numerico aleatorio de 7 digitos unico
    Parametros:
        catalogo: lista de diccionarios de videojuegos existentes
    Retorna:
        Codigo entero de 7 digitos no repetido
    """
    codigos_existentes = []
    for juego in catalogo:
        codigos_existentes.append(juego["codigo_identificador"])

    codigo = random.randint(1000000, 9999999)
    while codigo in codigos_existentes:
        codigo = random.randint(1000000, 9999999)

    return codigo


def normalizar_genero(texto: str) -> str:
    """
    Normaliza el texto ingresado para un genero y lo compara contra los validos.
    Parametros:
        texto: cadena ingresada por consola.
    Retorna:
        Nombre del genero con formato valido o cadena vacia si no coincide.
    """
    limpio = texto.strip().lower()
    resultado = ""

    for genero in GENEROS_VALIDOS:
        if genero.lower() == limpio:
            resultado = genero

    return resultado


def normalizar_sentido_orden(texto: str) -> str:
    """
    Normaliza la entrada de ordenamiento a 'ASCENDENTE' o 'DESCENDENTE'
    Parametros:
        texto: cadena ingresada por consola (ej. 'asc', 'aSC', 'DeSc')
    Retorna:
        'ASCENDENTE', 'DESCENDENTE' o cadena vacia si no es valida
    """
    limpio = texto.strip().lower()
    resultado = ""

    if limpio == ("asc"):
        resultado = "ASCENDENTE"
    elif limpio == ("desc"):
        resultado = "DESCENDENTE"

    return resultado

def pedir_nombre_valido() -> str:
    """
    Solicita por consola un nombre de entre 3 y 50 caracteres
    Retorna:
        Nombre valido sin espacios extremos innecesarios
    """
    while True:
        nombre = input("Ingrese el nombre del videojuego (3 a 50 caracteres): ").strip()
        if 3 <= len(nombre) <= 50:
            return nombre
        print("Error: el nombre debe tener entre 3 y 50 caracteres")


def pedir_genero_valido() -> str:
    """
    Solicita y valida un genero dentro de los permitidos
    Retorna:
        Genero valido
    """
    while True:
        print(f"Generos disponibles: {', '.join(GENEROS_VALIDOS)}")
        entrada = input("Ingrese el genero: ")
        genero = normalizar_genero(entrada)
        if genero != "":
            return genero
        print("Error: genero invalido. Intente nuevamente")


def pedir_flotante_mayor_cero(mensaje: str) -> float:
    """
    Solicita un numero decimal mayor a 0 por consola
    Parametros:
        mensaje: texto mostrado al usuario
    Retorna:
        Numero flotante mayor a 0
    """
    while True:
        entrada = input(mensaje).strip().replace(",", ".")
        try:
            valor = float(entrada)
            if valor > 0:
                return valor
            print("Error: el valor debe ser mayor a 0")
        except:
            print("Error: debe ingresar un numero valido")


def pedir_entero_no_negativo(mensaje: str) -> int:
    """
    Solicita un numero entero mayor o igual a 0 por consola
    Parametros:
        mensaje: texto mostrado al usuario
    Retorna:
        Numero entero mayor o igual a 0
    """
    while True:
        entrada = input(mensaje).strip()
        try:
            valor = int(entrada)
            if valor >= 0:
                return valor
            print("Error: el valor no puede ser negativo")
        except:
            print("Error: debe ingresar un numero entero valido")


def mostrar_juego(juego: dict) -> None:
    """
    Muestra por consola todos los datos de un videojuego
    Parametros:
        juego: diccionario con los datos del videojuego
    """
    print(
        f"Codigo: {juego['codigo_identificador']} | "
        f"Nombre: {juego['nombre']} | "
        f"Genero: {juego['genero']} | "
        f"Precio: ${juego['precio']:.2f} | "
        f"Stock: {juego['stock']} | "
        f"Vendidos: {juego['unidades_vendidas']}"
    )


def dar_de_alta_juego(catalogo: list, ruta_archivo: str) -> None:
    """
    Da de alta un videojuego con codigo unico de 7 digitos y actualiza el CSV
    Parametros:
        catalogo: lista de diccionarios de videojuegos
        ruta_archivo: ruta del archivo CSV a actualizar
    """
    print("--- ALTA DE VIDEOJUEGO ---")
    codigo = generar_codigo_unico(catalogo)
    nombre = pedir_nombre_valido()
    genero = pedir_genero_valido()
    precio = pedir_flotante_mayor_cero("Ingrese el precio (mayor a 0): ")
    stock = pedir_entero_no_negativo("Ingrese el stock inicial (0 o mayor): ")

    nuevo_juego = {
        "codigo_identificador": codigo,
        "nombre": nombre,
        "genero": genero,
        "precio": precio,
        "stock": stock,
        "unidades_vendidas": 0,
    }

    catalogo.append(nuevo_juego)
    guardar_juegos_csv(ruta_archivo, catalogo)
    print(f"Juego dado de alta con exito. Codigo asignado: {codigo}")


def registrar_venta(catalogo: list, ruta_archivo: str) -> None:
    """
    Muestra juegos con stock mayor a 0, valida codigo y cantidad, y actualiza el CSV
    Parametros:
        catalogo: lista de diccionarios de videojuegos
        ruta_archivo: ruta del archivo CSV a guardar
    """
    print("--- REGISTRAR VENTA ---")
    hay_stock = False

    for juego in catalogo:
        if juego["stock"] > 0:
            hay_stock = True
            print(f"Codigo: {juego['codigo_identificador']} | Nombre: {juego['nombre']} | Stock: {juego['stock']}")

    if hay_stock:
        codigo_ingresado = int(input("Ingrese el codigo identificador: "))
        juego_elegido = None

        for juego in catalogo:
            if juego["stock"] > 0 and juego["codigo_identificador"] == codigo_ingresado:
                juego_elegido = juego

        if juego_elegido is not None:
            cantidad = int(input("Ingrese la cantidad vendida: "))
            if 0 < cantidad <= juego_elegido["stock"]:
                juego_elegido["stock"] -= cantidad
                juego_elegido["unidades_vendidas"] += cantidad
                guardar_juegos_csv(ruta_archivo, catalogo)
                print("Venta registrada.")
            else:
                print("Cantidad invalida.")
        else:
            print("Codigo no valido o sin stock.")
    else:
        print("No hay juegos con stock.")
    return

def mostrar_estadisticas(catalogo: list) -> None:
    """
    Calcula y muestra las 5 estadisticas requeridas sobre el catalogo
    ★ Videojuego más vendido.
    ★ Género con mayor cantidad de unidades vendidas.
    ★ Valor total del inventario (stock * precio).
    ★ Porcentaje de videojuegos sin stock.
    ★ Promedio de precios por género.
    Parametros:
        catalogo: lista de diccionarios de videojuegos
    """
    print("--- ESTADISTICAS ---")
    if len(catalogo) == 0:
        print("El catalogo esta vacio. No hay estadisticas para mostrar")
        return

    mas_vendido = catalogo[0]
    for juego in catalogo:
        if juego["unidades_vendidas"] > mas_vendido["unidades_vendidas"]:
            mas_vendido = juego

    print(
        f"1. Videojuego mas vendido: {mas_vendido['nombre']} "
        f"({mas_vendido['unidades_vendidas']} unidades)"
    )

    ventas_por_genero = {}
    for genero in GENEROS_VALIDOS:
        ventas_por_genero[genero] = 0

    for juego in catalogo:
        genero = juego["genero"]
        if genero in ventas_por_genero:
            ventas_por_genero[genero] += juego["unidades_vendidas"]

    mejor_genero = GENEROS_VALIDOS[0]
    for genero in GENEROS_VALIDOS:
        if ventas_por_genero[genero] > ventas_por_genero[mejor_genero]:
            mejor_genero = genero

    print(
        f"2. Genero con mayor cantidad de unidades vendidas: {mejor_genero} "
        f"({ventas_por_genero[mejor_genero]} unidades)"
    )

    valor_total = 0.0
    for juego in catalogo:
        valor_total += juego["stock"] * juego["precio"]

    print(f"3. Valor total del inventario: ${valor_total:.2f}")

    sin_stock = 0
    for juego in catalogo:
        if juego["stock"] == 0:
            sin_stock += 1

    porcentaje_sin_stock = (sin_stock / len(catalogo)) * 100
    print(f"4. Porcentaje de videojuegos sin stock: {porcentaje_sin_stock:.2f}%")

    print("5. Promedio de precios por genero:")
    for genero in GENEROS_VALIDOS:
        suma_precios = 0.0
        cantidad_juegos = 0
        for juego in catalogo:
            if juego["genero"] == genero:
                suma_precios += juego["precio"]
                cantidad_juegos += 1

        if cantidad_juegos > 0:
            promedio = suma_precios / cantidad_juegos
            print(f" - {genero}: ${promedio:.2f}")
        else:
            print(f" - {genero}: Sin juegos cargados")


def ordenar_juegos(catalogo: list, campo: str, criterio: str) -> list:
    """
    Ordena una copia de la lista de videojuegos segun campo y criterio usando for anidados
    Parametros:
        catalogo: lista de diccionarios de videojuegos
        campo: clave por la que se ordena ('nombre', 'genero' o 'precio')
        criterio: 'ASCENDENTE' o 'DESCENDENTE'
    Retorna:
        Nueva lista ordenada segun el criterio indicado
    """
    lista_ordenada = []
    for juego in catalogo:
        lista_ordenada.append(juego)

    for i in range(len(lista_ordenada) - 1):
        for j in range(i + 1, len(lista_ordenada)):
            valor_i = lista_ordenada[i][campo]
            valor_j = lista_ordenada[j][campo]
            
            if criterio == "ASCENDENTE" and valor_i > valor_j:
                intercambiar_elementos(lista_ordenada, i, j)
            elif criterio == "DESCENDENTE" and valor_i < valor_j:
                intercambiar_elementos(lista_ordenada, i, j)

    return lista_ordenada


def mostrar_catalogo_ordenado(catalogo: list) -> None:
    """
    Solicita criterio y sentido de ordenamiento y muestra todo el catalogo ordenado
    Parametros:
        catalogo: lista de diccionarios de videojuegos
    """
    print("--- CATALOGO ORDENADO ---")
    if len(catalogo) == 0:
        print("El catalogo esta vacio")
        return

    while True:
        campo_ingresado = input("Ordenar por (nombre, genero o precio): ")
        if campo_ingresado != "":
            break
        print("Error: criterio invalido. Elija entre nombre, genero o precio")

    while True:
        criterio_ingresado = input("Sentido de ordenamiento (asc / desc): ")
        criterio = normalizar_sentido_orden(criterio_ingresado)
        if criterio != "":
            break
        print("Error: sentido invalido. Ingrese asc o desc")

    ordenada = ordenar_juegos(catalogo, campo_ingresado, criterio)
    for juego in ordenada:
        mostrar_juego(juego)