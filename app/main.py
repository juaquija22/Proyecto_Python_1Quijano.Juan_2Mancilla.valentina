"""
Autor: Juan Pablo Quijano y valentina mancilla
Fecha: 28/07/2025
Descripción: Administrador de Colección de Libros/Películas/Música
"""

import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import utils.screencontrollers as sc
import controllers.menu as mn


def main_menu():
    while True:
        sc.limpiar_pantalla()
        print('========================================')
        print('Administrador de Colección')
        print('========================================')
        print('1. Añadir un Nuevo Elemento')
        print('2. Ver Todos los Elementos')
        print('3. Buscar un Elemento')
        print('4. Editar un Elemento')
        print('5. Eliminar un Elemento')
        print('6. Ver Elementos por Categoría')
        print('7. Salir')
        print('========================================')

        try:
            op = int(input("\nElige una opción (1-7): "))
            if 1 <= op <= 7:
                return op
        except ValueError:
            pass  

        print("\nOpción no válida. Intenta nuevamente.")
        sc.pausar()


if __name__ == "__main__":
    while True:
        opcion = main_menu()

        if opcion == 1:
            mn.main_menu_añadir()
        elif opcion == 2:
            mn.main_menu_ver_elementos()
        elif opcion == 3:
            mn.main_menu_buscar()
        elif opcion == 4:
            mn.main_menu_editar()
        elif opcion == 5:
            mn.main_menu_eliminar_elementos()
        elif opcion == 6:
            mn.main_menu_elementos_categoria()
        elif opcion == 7:
            break
