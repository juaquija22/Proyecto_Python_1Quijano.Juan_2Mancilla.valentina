from utils.corefiles import readJson, updateJson
import utils.screencontrollers as sc

def editar_titulo_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    coincidencias = []

    for archivo in archivos:
        data = readJson(archivo)
        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    coincidencias.append({
                        "archivo": archivo,
                        "categoria": categoria,
                        "id": id_elemento,
                        "item": item
                    })

    if not coincidencias:
        print("No se encontró un elemento con ese nombre.")
        sc.pausar()
        return

    print("\nElementos encontrados:")
    for idx, match in enumerate(coincidencias, 1):
        print(f"{idx}. [{match['archivo']} - {match['categoria']}] ID: {match['id']}")
        print(f"   Detalles: {match['item']}")

    while True:
        seleccion = input("Ingresa el número del elemento que deseas editar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(coincidencias):
            break
        else:
            print("Selección inválida. Intenta de nuevo.")

    elegido = coincidencias[int(seleccion) - 1]
    nuevo_nombre = input("Ingresa el nuevo título: ")

    updateJson(
        {"nombre": nuevo_nombre},
        path_keys=[elegido["categoria"], elegido["id"]],
        filename=elegido["archivo"]
    )
    print("Título actualizado correctamente.")
    sc.pausar()


def editar_autor_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    coincidencias = []

    for archivo in archivos:
        data = readJson(archivo)
        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    coincidencias.append({
                        "archivo": archivo,
                        "categoria": categoria,
                        "id": id_elemento,
                        "item": item
                    })

    if not coincidencias:
        print("No se encontró un elemento con ese nombre.")
        sc.pausar()
        return

    print("\nElementos encontrados:")
    for idx, match in enumerate(coincidencias, 1):
        print(f"{idx}. [{match['archivo']} - {match['categoria']}] ID: {match['id']}")
        print(f"   Detalles: {match['item']}")

    while True:
        seleccion = input("Ingresa el número del elemento que deseas editar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(coincidencias):
            break
        else:
            print("Selección inválida. Intenta de nuevo.")

    elegido = coincidencias[int(seleccion) - 1]
    nuevo_autor = input("Ingresa el nuevo autor/director/artista: ")

    updateJson(
        {"autor": nuevo_autor},
        path_keys=[elegido["categoria"], elegido["id"]],
        filename=elegido["archivo"]
    )
    print("Autor actualizado correctamente.")
    sc.pausar()


def editar_genero_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    coincidencias = []

    for archivo in archivos:
        data = readJson(archivo)
        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    coincidencias.append({
                        "archivo": archivo,
                        "categoria": categoria,
                        "id": id_elemento,
                        "item": item
                    })

    if not coincidencias:
        print("No se encontró un elemento con ese nombre.")
        sc.pausar()
        return

    print("\nElementos encontrados:")
    for idx, match in enumerate(coincidencias, 1):
        print(f"{idx}. [{match['archivo']} - {match['categoria']}] ID: {match['id']}")
        print(f"   Detalles: {match['item']}")

    while True:
        seleccion = input("Ingresa el número del elemento que deseas editar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(coincidencias):
            break
        else:
            print("Selección inválida. Intenta de nuevo.")

    elegido = coincidencias[int(seleccion) - 1]
    nuevo_genero = input("Ingresa el nuevo género: ")

    updateJson(
        {"genero": nuevo_genero},
        path_keys=[elegido["categoria"], elegido["id"]],
        filename=elegido["archivo"]
    )
    print("Género actualizado correctamente.")
    sc.pausar()


def editar_calificacion_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    coincidencias = []

    for archivo in archivos:
        data = readJson(archivo)
        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    coincidencias.append({
                        "archivo": archivo,
                        "categoria": categoria,
                        "id": id_elemento,
                        "item": item
                    })

    if not coincidencias:
        print("No se encontró un elemento con ese nombre.")
        sc.pausar()
        return

    print("\nElementos encontrados:")
    for idx, match in enumerate(coincidencias, 1):
        print(f"{idx}. [{match['archivo']} - {match['categoria']}] ID: {match['id']}")
        print(f"   Detalles: {match['item']}")

    while True:
        seleccion = input("Ingresa el número del elemento que deseas editar: ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(coincidencias):
            break
        else:
            print("Selección inválida. Intenta de nuevo.")

    elegido = coincidencias[int(seleccion) - 1]

    while True:
        try:
            nueva_calificacion = int(input("Ingrese la nueva calificación (1 a 10): "))
            if 1 <= nueva_calificacion <= 10:
                updateJson(
                    {"calificacion": nueva_calificacion},
                    path_keys=[elegido["categoria"], elegido["id"]],
                    filename=elegido["archivo"]
                )
                print("Calificación actualizada correctamente.")
                break
            else:
                print("La calificación debe estar entre 1 y 10.")
        except ValueError:
            print("La calificación debe ser un número.")

    sc.pausar()
