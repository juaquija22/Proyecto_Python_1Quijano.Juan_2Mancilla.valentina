import utils.corefiles as cf
import utils.screencontrollers as sc
from tabulate import tabulate


def listar_libros():
    sc.limpiar_pantalla()
    datos = cf.readJson("libros.json")

    if "libros" not in datos or not datos["libros"]:
        print("No hay libros registrados.")
        sc.pausar()
        return

    print("=== Lista de Libros Registrados ===")
    headers = ["ID", "Nombre", "Autor", "Género", "Calificación"]
    table = []

    for idbk, info in datos["libros"].items():
        table.append([
            idbk,
            info.get("nombre", "N/A"),
            info.get("autor", "N/A"),
            info.get("genero", "N/A"),
            f"{info.get('calificacion', 0)}/10"
        ])

    print(tabulate(table, headers, tablefmt="grid"))
    sc.pausar()


def listar_musica():
    sc.limpiar_pantalla()
    datos = cf.readJson("musica.json")

    if "musica" not in datos or not datos["musica"]:
        print("No hay canciones registradas.")
        sc.pausar()
        return

    print("=== Lista de Canciones Registradas ===")
    headers = ["ID", "Nombre", "Artista", "Género", "Calificación"]
    table = []

    for idms, info in datos["musica"].items():
        table.append([
            idms,
            info.get("nombre", "N/A"),
            info.get("autor", "N/A"),
            info.get("genero", "N/A"),
            f"{info.get('calificacion', 0)}/10"
        ])

    print(tabulate(table, headers, tablefmt="grid"))
    sc.pausar()


def listar_peliculas():
    sc.limpiar_pantalla()
    datos = cf.readJson("peliculas.json")

    if "peliculas" not in datos or not datos["peliculas"]:
        print("No hay películas registradas.")
        sc.pausar()
        return

    print("=== Lista de Películas Registradas ===")
    headers = ["ID", "Nombre", "Director", "Género", "Calificación"]
    table = []

    for idmv, info in datos["peliculas"].items():
        table.append([
            idmv,
            info.get("nombre", "N/A"),
            info.get("autor", "N/A"),
            info.get("genero", "N/A"),
            f"{info.get('calificacion', 0)}/10"
        ])

    print(tabulate(table, headers, tablefmt="grid"))
    sc.pausar()

  
