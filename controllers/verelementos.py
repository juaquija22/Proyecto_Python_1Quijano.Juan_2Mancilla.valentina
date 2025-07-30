import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from controllers.vermusica import main_menu_ver_musica
from controllers.verpeliculas import main_menu_ver_peliculas
from controllers.verlibros import main_menu_ver_libros
from utils. screencontrollers import limpiar_pantalla,pausar

def main_menu_ver_elementos():
        limpiar_pantalla()
        print('===========================================')
        print('ver elementos')
        print('===========================================')
        print('¿Que categoria deseas ver?')
        print('1. Ver Todos los Libros')
        print('2. Ver Todas las Películas')
        print('3. Ver Toda la Música')
        print('4.Regresar al Menú Principal')
        print('===========================================')
        print('Selecciona una opción (1-4):')
        opcion=input()
        if opcion =='1':
                from controllers.verlibros import main_menu_ver_libros
                main_menu_ver_libros()
        elif opcion == '2':
                from controllers.verelementos import main_menu_ver_peliculas
                main_menu_ver_peliculas()
        elif opcion == '3':
                from controllers.vermusica import main_menu_ver_musica
                main_menu_ver_musica()
        elif opcion == '4':
                from controllers.mainmenu import main_menu
                main_menu()
        else:
                print('opcion no valida intente de nuevo')
                pausar()
                main_menu_ver_elementos()


                
                
