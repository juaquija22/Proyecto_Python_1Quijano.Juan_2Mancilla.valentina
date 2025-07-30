"""
Autor: Juan Pablo Quijano y valentina mancilla
Fecha: 28/07/2025
Descripción: este proyecto consiste en una liga betplay donde se pueden hacer transferencias de jugadores crear jugadores crear equipos
"""

import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.screencontrollers as sc
import controllers.anadir as add
import controllers.listar as ls
import controllers.menu as mn


def main_menu():
    while True:
        sc.limpiar_pantalla()
        print ('========================================')
        print ('Administrador de Colección')
        print('===========================================')
        print('1. Añadir un Nuevo Elemento')
        print('2. Ver Todos los Elementos')
        print('3. Buscar un Elemento')
        print('4. Editar un Elemento')
        print('5. Eliminar un Elemento')
        print('6. Ver Elementos por Categoría')
        print('7. Guardar y Cargar Colección')
        print('8. Salir')
        print('===========================================')
        print('selecciona una opción (1-8):')
        try:
            op=int(input("\n elige una opcion :"))
            if 1 <= op <= 6:
                return op
        except:
                pass
        return None

if __name__ == "__main__":
        while True:
                opcion = main_menu()
                if opcion == 1:
                      mn.main_menu_añadir()   
                elif opcion == 2:
                      mn.main_menu_ver_elementos()
                     
                elif opcion == 3:
                      pass
                       
                elif opcion == 4:
                      pass
                       
                elif opcion == 5:
                      pass                 
                      
                       
                elif opcion == 6:
                       pass
                      
                elif opcion == 0:
                       
                       break
                else:
                       print ('\n Opcion no valida')
                       sc.pausar()
