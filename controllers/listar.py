import utils.corefiles as cf
import utils.screencontrollers as sc

def listar_libros():
    sc.limpiar_pantalla()
    datos = cf.readJson("libro.json")

    if "libro" not in datos or not datos["libro"]:
        print("No hay libros registrados.")
        sc.pausar()
        return

    print("=== Lista de Libros Registrados ===")
    for idbk, info in datos["libro"].items():
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
        print(f"Título: {info['titulo']}")
        print(f"Artista: {info['artista']}")
        print(f"Género: {info['genero']}")
        print(f"Calificación: {info['calificacion']}/10")
    
    sc.pausar()



def listar_peliculas():
    sc.limpiar_pantalla()
    datos = cf.readJson("pelicula.json")  

    if "pelicula" not in datos or not datos["pelicula"]:
        print("No hay películas registradas.")
        sc.pausar()
        return

    print("=== Lista de Películas Registradas ===")
    for idpl, info in datos["pelicula"].items():
        print(f"\nID: {idpl}")
        print(f"Título: {info['titulo']}")
        print(f"Director: {info['director']}")
        print(f"Género: {info['genero']}")
        print(f"Calificación: {info['calificacion']}/10")
    
    sc.pausar()