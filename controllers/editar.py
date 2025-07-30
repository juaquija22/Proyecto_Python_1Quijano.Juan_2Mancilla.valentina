from utils.corefiles import readJson, updateJson
import utils.screencontrollers as sc

def editar_titulo_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)

        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    print(f"\nElemento encontrado en {archivo} > {categoria} > ID {id_elemento}:")
                    print(item)

                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    updateJson({"nombre": nuevo_nombre}, path_keys=[categoria, id_elemento], filename=archivo)
                    print("Nombre actualizado correctamente.")
                    sc.pausar()
                    return

    print("No se encontró un elemento con ese nombre.")
    sc.pausar()


def editar_autor_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)

        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    print(f"\nElemento encontrado en {archivo} > {categoria} > ID {id_elemento}:")
                    print(item)

                    nuevo_autor = input("Ingrese el nuevo autor/director/artista: ")
                    updateJson({"autor": nuevo_autor}, path_keys=[categoria, id_elemento], filename=archivo)
                    print("Autor actualizado correctamente.")
                    sc.pausar()
                    return

    print("No se encontró un elemento con ese nombre.")
    sc.pausar()


def editar_genero_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)

        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    print(f"\nElemento encontrado en {archivo} > {categoria} > ID {id_elemento}:")
                    print(item)

                    nuevo_genero = input("Ingrese el nuevo género: ")
                    updateJson({"genero": nuevo_genero}, path_keys=[categoria, id_elemento], filename=archivo)
                    print("Género actualizado correctamente.")
                    sc.pausar()
                    return

    print("No se encontró un elemento con ese nombre.")
    sc.pausar()


def editar_calificacion_por_nombre():
    sc.limpiar_pantalla()
    nombre_buscado = input("Ingresa el nombre del elemento a editar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)

        for categoria, elementos in data.items():
            for id_elemento, item in elementos.items():
                if "nombre" in item and nombre_buscado in item["nombre"].lower():
                    print(f"\nElemento encontrado en {archivo} > {categoria} > ID {id_elemento}:")
                    print(item)

                    try:
                        nueva_calificacion = int(input("Ingrese la nueva calificación (número): "))
                        updateJson({"calificacion": nueva_calificacion}, path_keys=[categoria, id_elemento], filename=archivo)
                        print("calificación actualizada correctamente.")
                    except ValueError:
                        print("La calificación debe ser un número.")
                    sc.pausar()
                    return

    print("No se encontró un elemento con ese nombre.")
    sc.pausar()