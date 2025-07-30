import json
from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd
from config import DB_PATH
import random
import os




def add_elemento():
    sc.limpiar_pantalla()
    match main_menu:
        case 1:
            books()


    if not cf.updateJson(eq, ["equipos", "equipos"]):
        print("Equipo agregado exitosamente")
    else:
        print("No se pudo agregar el equipo")
    
    sc.pausar()

def main_menu():
    while True:
        limpiar_pantalla()
        print('===========================================')
        print(' Añadir un Nuevo Elemento')
        print('===========================================')
        print(' tipo de elemento deseas añadir?')
        print('1. Libro')
        print('2. Película')
        print('3. Música')
        print('4. Regresar al Menú Principal')
        print('===========================================')
        print('seleccione una opción (1-4):')
        try:
            op=int(input("\n elige una opcion :"))
            if 1 <= op <= 6:
                return op
        except:
                pass
        return None






def add_book():
    sc.limpiar_pantalla()
    idbk = random.randint(1023, 9876)
    Bookname = vd.validatetext('Nombre Del Libro :')
    Creator = vd.validatetext('Nombre Del Autor :')
    Gender = vd.validatetext('Genero Del Libro :')
    score = vd.validateInt('Valoracion del Libro (1-10) :')
    if score < 10 and score > 1:
        pass
    else: 
        print('Numero Invalido')
    libro_data = {
        idbk: {
            "nombre": Bookname,
            "autor": Creator,
            "genero": Gender,
            "calificacion": score,
        }
    }

    if not cf.updateJson(libro_data, ["libro", "Libros"]):
        print("Equipo agregado exitosamente")
    else:
        print("No se pudo agregar el equipo")
    
    sc.pausar()



def add_movie():
    sc.limpiar_pantalla()
    idmv = random.randint(1023, 9876)
    moviename = vd.validatetext('Nombre De La Pelicula :')
    Creator = vd.validatetext('Nombre Del Autor :')
    Gender = vd.validatetext('Genero De la Pelicula :')
    score = vd.validateInt('Valoracion de la Pelicula (1-10) :')
    if score < 10 and score > 1:
        pass
    else: 
        print('Numero Invalido')
        sc.pausar
        return
    Movie_data = {
        idmv: {
            "nombre": moviename,
            "autor": Creator,
            "genero": Gender,
            "calificacion": score,
        }
    }

    if not cf.updateJson(Movie_data, ["pelicula", "Peliculas"]):
        print("Pelicula agregada exitosamente")
    else:
        print("No se pudo agregar la Pelicula")
    
    sc.pausar()



def add_music():
    sc.limpiar_pantalla()
    idms = random.randint(1023, 9876)
    musicname = vd.validatetext('Nombre De La Cancion :')
    Creator = vd.validatetext('Nombre Del Autor :')
    Gender = vd.validatetext('Genero De la Cancion :')
    score = vd.validateInt('Valoracion de la Cancion (1-10) :')
    if score < 10 and score > 1:
        pass
    else: 
        print('Numero Invalido')
        sc.pausar
        return
    Music_data = {
        idms: {
            "nombre": musicname,
            "autor": Creator,
            "genero": Gender,
            "calificacion": score,
        }
    }

    if not cf.updateJson(Music_data, ["musica", "Musica"]):
            print("Cancion agregado exitosamente")
    else:
        print("No se pudo agregar La cancion")
    
    sc.pausar()
