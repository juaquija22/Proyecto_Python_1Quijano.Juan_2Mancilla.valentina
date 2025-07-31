import utils.screencontrollers as sc
import controllers.anadir as add
import controllers.listar as ls
import controllers.buscar as bs
import controllers.editar as ed
import controllers.eliminar as el
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

def main_menu_buscar():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        Buscar un Elemento')
        print('===========================================')
        print('¿Cómo deseas buscar?')
        print('1. Buscar por Título')
        print('2. Buscar por Autor/Director/Artista')
        print('3. Buscar por Género')
        print('4. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-4): '))
            if op == 1:
                bs.buscar_por_titulo()
                

            elif op == 2:
                bs.buscar_por_autor()

            elif op == 3:
                bs.buscar_por_genero()

            elif op == 4:
                print("\nRegresando al menú principal...")
                break
            else:
                print('\nOpción no válida. Intenta de nuevo.')
                sc.pausar()
        except ValueError:
            print("\nEntrada no válida. Por favor, introduce un número.")
            sc.pausar()

def main_menu_editar():
    while True:
        sc.limpiar_pantalla()
        print('===========================================')
        print('        Editar un Elemento')
        print('===========================================')
        print('¿Qué tipo de cambio deseas realizar?')
        print('1. Editar Título')
        print('2. Editar Autor/Director/Artista')
        print('3. Editar Género')
        print('4. Editar Valoración')
        print('5. Regresar al Menú Principal')
        print('===========================================')

        try:
            op = int(input('\nSelecciona una opción (1-5): '))
            if op == 1:
                ed.editar_titulo_por_nombre()
                
            elif op == 2:
                ed.editar_autor_por_nombre()
                
            elif op == 3:
                ed.editar_genero_por_nombre()
                
            elif op == 4:
                ed.editar_calificacion_por_nombre()
                
            elif op == 5:
                print("\nRegresando al menú principal...")
                break
            else:
                print('\nOpción no válida. Intenta de nuevo.')
                sc.pausar()
        except ValueError:
            print('\nEntrada inválida. Por favor, introduce un número.')
            sc.pausar()






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
                el.eliminar_por_titulo()

            elif opcion == 2:
               el.eliminar_por_id()

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








