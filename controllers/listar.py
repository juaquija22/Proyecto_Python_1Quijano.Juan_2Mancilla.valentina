import utils.corefiles as cf
import utils.screencontrollers as sc

def listar_libros():
    sc.limpiar_pantalla()
    datos = cf.readJson("libros.json")

    if "libros" not in datos or not datos["libros"]:
        print("No hay libros registrados.")
        sc.pausar()
        return

    print("=== Lista de Libros Registrados ===")
    for idbk, info in datos["libros"].items():
        print(f"\nID: {idbk}")
        print(f"Nombre: {info['nombre']}")
        print(f"Autor: {info['autor']}")
        print(f"Género: {info['genero']}")
        print(f"Calificación: {info['calificacion']}/10")
    
    sc.pausar()





def listar_musica():
    sc.limpiar_pantalla()
    datos = cf.readJson("musica.json")

    if "musica" not in datos or not datos["musica"]:
        print("No hay canciones registradas.")
        sc.pausar()
        return

    print("=== Lista de Canciones Registradas ===")
    for idms, info in datos["musica"].items():
        print(f"\nID: {idms}")
        print(f"Nombre: {info['nombre']}")
        print(f"Artista: {info['autor']}")
        print(f"Género: {info['genero']}")
        print(f"Calificación: {info['calificacion']}/10")

    sc.pausar()




def listar_peliculas():
    sc.limpiar_pantalla()
    datos = cf.readJson("peliculas.json")

    if "peliculas" not in datos or not datos["peliculas"]:
        print("No hay películas registradas.")
        sc.pausar()
        return

    print("=== Lista de Películas Registradas ===")
    for idmv, info in datos["peliculas"].items():
        print(f"\nID: {idmv}")
        print(f"Nombre: {info['nombre']}")
        print(f"Director: {info['autor']}")
        print(f"Género: {info['genero']}")
        print(f"Calificación: {info['calificacion']}/10")
    
    sc.pausar()
