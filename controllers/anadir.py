import json
from utils.screencontrollers import limpiar_pantalla
from utils.screencontrollers import pausar
import utils.corefiles as cf
import utils.screencontrollers as sc
import utils.validatedata as vd
from config import DB_PATH
import random
import os

            



def add_book():
    sc.limpiar_pantalla()
    idbk = random.randint(1023, 9876)
    
    Bookname = vd.validatetext('Nombre Del Libro :')
    Creator = vd.validatetext('Nombre Del Autor :')
    Gender = vd.validatetext('Genero Del Libro :')
    score = vd.validateInt('Valoración del Libro (1-10) :')
    
    if not (1 <= score <= 10):
        print('Número inválido. Debe estar entre 1 y 10.')
        sc.pausar()
        return
    
    libro_data = {
        idbk: {
            "nombre": Bookname,
            "autor": Creator,
            "genero": Gender,
            "calificacion": score,
        }
    }

    if cf.updateJson(libro_data, ["libro"]):
        print("Libro agregado exitosamente.")
    else:
        print("No se pudo agregar el libro.")
    
    sc.pausar()




def add_movie():
    sc.limpiar_pantalla()
    idmv = random.randint(1023, 9876)
    
    title = vd.validatetext('Nombre de la Película :')
    director = vd.validatetext('Director :')
    genre = vd.validatetext('Género :')
    rating = vd.validateInt('Calificación (1-10) :')
    
    if not (1 <= rating <= 10):
        print('Número inválido. Debe estar entre 1 y 10.')
        sc.pausar()
        return

    movie_data = {
        idmv: {
            "nombre": title,
            "director": director,
            "genero": genre,
            "calificacion": rating,
        }
    }

    if cf.updateJson(movie_data, ["pelicula"]):
        print("Película agregada exitosamente.")
    else:
        print("No se pudo agregar la película.")
    
    sc.pausar()





def add_music():
    sc.limpiar_pantalla()
    idmsc = random.randint(1023, 9876)
    
    title = vd.validatetext('Nombre de la Canción :')
    artist = vd.validatetext('Artista :')
    genre = vd.validatetext('Género :')
    rating = vd.validateInt('Calificación (1-10) :')
    
    if not (1 <= rating <= 10):
        print('Número inválido. Debe estar entre 1 y 10.')
        sc.pausar()
        return

    music_data = {
        idmsc: {
            "nombre": title,
            "artista": artist,
            "genero": genre,
            "calificacion": rating,
        }
    }

    if cf.updateJson(music_data, ["musica"]):
        print("Canción agregada exitosamente.")
    else:
        print("No se pudo agregar la canción.")
    
    sc.pausar()
