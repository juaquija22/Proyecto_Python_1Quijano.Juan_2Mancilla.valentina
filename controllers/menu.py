import os
import sys
import utils.screencontrollers as sc
import controllers.anadir as add
import controllers.listar as ls


def main_menu_añadir():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        Añadir un Nuevo Elemento')
        print('===========================================')
        print('¿Qué tipo de elemento deseas añadir?')
        print('1. Libro')
        print('2. Película')
        print('3. Música')
        print('4. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-4): '))
            if op == 1:
                add.add_book()
                
            elif op == 2:
                add.add_movie()
                
            elif op == 3:
                add.add_music()
                
            elif op == 4:
                print("\nRegresando al menú principal...")
                break
        except ValueError:
            print('\nEntrada inválida. Por favor, introduce un número.')
            sc.pausar()


        

        
  

def main_menu_ver_elementos():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('          Ver Todos los Elementos')
        print('===========================================')
        print('¿Qué categoría deseas ver?')
        print('1. Ver Todos los Libros')
        print('2. Ver Todas las Películas')
        print('3. Ver Toda la Música')
        print('4. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-4): '))
            if opcion == 1:
                ls.listar_libros()
                

            elif opcion == 2:
                ls.listar_peliculas()
                

            elif opcion == 3:
                ls.listar_musica()
                

            elif opcion == 4:
                print("\nRegresando al menú principal...")
                break

        except ValueError:
            print('\nEntrada no válida. Por favor, ingresa un número.')
            sc.pausar
            



                       
    


'''
def main_menu_eliminar_elementos():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('         Eliminar un Elemento')
        print('===========================================')
        print('¿Cómo deseas eliminar?')
        print('1. Eliminar por Título')
        print('2. Eliminar por Identificador Único')
        print('3. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-3): '))
            
            if opcion == 1:
                
                try:
                    from controllers.eliminarportitulo import eliminar_por_titulo
                    eliminar_por_titulo()
                except ImportError:
                    print("Error: No se pudo importar eliminar_por_titulo.")
                    sc.pausar()

            elif opcion == 2:
                try:
                    from controllers.eliminarporid import eliminar_por_id
                    eliminar_por_id()
                except ImportError:
                    print("Error: No se pudo importar eliminar_por_id.")
                    sc.pausar()

            elif opcion == 3:
                print("\nRegresando al menú principal...")
                break  

            else:
                print("\nOpción no válida. Por favor, ingresa un número del 1 al 3.")
                sc.pausar()

        except ValueError:
            print('\nEntrada no válida. Por favor, ingresa un número.')
            sc.pausar()                                 
          
                                
                
def main_menu_elementos_categoria():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        ¿Qué categoría deseas ver?')
        print('===========================================')
        print('1. Libros')
        print('2. Películas')
        print('3. Música')
        print('4. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-4): '))

            if opcion == 1:
                print("\nMostrando la categoría: LIBROS")
              
            elif opcion == 2:
                print("\nMostrando la categoría: PELÍCULAS")
              
            elif opcion == 3:
                print("\nMostrando la categoría: MÚSICA")
                
            elif opcion == 4:
                print("\nRegresando al menú principal...")
                break
        except ValueError:
            print("\nEntrada no válida. Por favor, ingresa un número del 1 al 4.")

        sc.pausar()



def main_menu_guardar_coleccion():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        Guardar y Cargar Colección')
        print('===========================================')
        print('¿Qué deseas hacer?')
        print('1. Guardar la Colección Actual')
        print('2. Cargar la Colección desde un Archivo')
        print('3. Regresar al Menú Principal')
        print('===========================================')

        try:
            opcion = int(input('\nSelecciona una opción (1-3): '))

            if opcion == 1:
                print("\nGuardando la colección actual...")
                
            elif opcion == 2:
                print("\nCargando la colección desde archivo...")
               
            elif opcion == 3:
                print("\nRegresando al menú principal...")
                break
            else:
                print("\nOpción no válida. Por favor, elige un número del 1 al 3.")
        except ValueError:
            print("\nEntrada no válida. Por favor, introduce un número.")
            sc.pausar'''