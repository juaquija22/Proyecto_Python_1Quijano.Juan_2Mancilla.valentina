import utils.corefiles as cf
import utils.screencontrollers as sc
from tabulate import tabulate


def mostrar_categoria_libros():
    sc.limpiar_pantalla()
    datos = cf.readJson("libros.json")

    if not datos or not datos.get("libros"):
        print("No hay libros registrados.")
        sc.pausar()
        return

    genero_filtrar = input("Ingresa el género  (ej. infantil, miedo, romance): ").strip().lower()

    print(f"=== Categoría Seleccionada: LIBROS - Género: {genero_filtrar} ===")
    headers = ["ID", "Nombre", "Autor", "Género", "Calificación"]
    tabla = []

    for id_libro, info in datos["libros"].items():
        genero = info.get("genero", "").lower()
        if genero_filtrar in genero:
            tabla.append([
                id_libro,
                info.get("nombre", "N/A"),
                info.get("autor", "N/A"),
                info.get("genero", "N/A"),
                f"{info.get('calificacion', 0)}/10"
            ])

    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron libros con ese género.")

    sc.pausar()


def mostrar_categoria_peliculas():
    sc.limpiar_pantalla()
    datos = cf.readJson("peliculas.json")

    if not datos or not datos.get("peliculas"):
        print("No hay películas registradas.")
        sc.pausar()
        return

    genero_filtrar = input("Ingresa el género  (ej. infantil, miedo, acción): ").strip().lower()

    print(f"=== Categoría Seleccionada: PELÍCULAS - Género: {genero_filtrar} ===")
    headers = ["ID", "Nombre", "Autor", "Género", "Calificación"]
    tabla = []

    for id_peli, info in datos["peliculas"].items():
        genero = info.get("genero", "").lower()
        if genero_filtrar in genero:
            tabla.append([
                id_peli,
                info.get("nombre", "N/A"),
                info.get("autor", "N/A"),
                info.get("genero", "N/A"),
                f"{info.get('calificacion', 0)}/10"
            ])

    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron películas con ese género.")

    sc.pausar()


def mostrar_categoria_musica():
    sc.limpiar_pantalla()
    datos = cf.readJson("musica.json")

    if not datos or not datos.get("musica"):
        print("No hay canciones registradas.")
        sc.pausar()
        return

    genero_filtrar = input("Ingresa el género  (ej. rock, pop, jazz): ").strip().lower()

    print(f"=== Categoría Seleccionada: MÚSICA - Género: {genero_filtrar} ===")
    headers = ["ID", "Nombre", "Autor", "Género", "Calificación"]
    tabla = []

    for id_musica, info in datos["musica"].items():
        genero = info.get("genero", "").lower()
        if genero_filtrar in genero:
            tabla.append([
                id_musica,
                info.get("nombre", "N/A"),
                info.get("autor", "N/A"),
                info.get("genero", "N/A"),
                f"{info.get('calificacion', 0)}/10"
            ])

    if tabla:
        print(tabulate(tabla, headers=headers, tablefmt="grid"))
    else:
        print("No se encontraron canciones con ese género.")

    sc.pausar()
