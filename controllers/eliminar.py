from utils.corefiles import readJson, writeJson
import utils.screencontrollers as sc

def eliminar_por_titulo():
    sc.limpiar_pantalla()
    titulo_buscado = input("Ingresa el título del elemento a eliminar: ").lower()
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)
        eliminado = False

        for categoria in data:
            ids_a_eliminar = []

            for id_elemento, item in data[categoria].items():
                if "nombre" in item and titulo_buscado in item["nombre"].lower():
                    print(f"Elemento encontrado en {archivo} > {categoria} > ID {id_elemento}:")
                    print(item)
                    confirmar = input("¿Deseas eliminar este elemento? (s/n): ").lower()
                    if confirmar == "s":
                        ids_a_eliminar.append(id_elemento)
                        eliminado = True

            for id_eliminar in ids_a_eliminar:
                del data[categoria][id_eliminar]

        if eliminado:
            writeJson(data, archivo)
            print(f"Elemento(s) eliminado(s) de {archivo} correctamente.")
            sc.pausar()
            return

    print("No se encontró ningún elemento con ese título.")
    sc.pausar()




    
def eliminar_por_id():
    sc.limpiar_pantalla()
    id_buscado = input("Ingresa el ID del elemento a eliminar: ")
    archivos = ["libros.json", "musica.json", "peliculas.json"]

    for archivo in archivos:
        data = readJson(archivo)
        eliminado = False

        for categoria in data:
            if id_buscado in data[categoria]:
                print(f"Elemento encontrado en {archivo} > {categoria} > ID {id_buscado}:")
                print(data[categoria][id_buscado])
                confirmar = input("¿Deseas eliminar este elemento? (s/n): ").lower()
                if confirmar == "s":
                    del data[categoria][id_buscado]
                    eliminado = True

        if eliminado:
            writeJson(data, archivo)
            print(f"Elemento con ID {id_buscado} eliminado correctamente de {archivo}.")
            sc.pausar()
            return

    print("No se encontró ningún elemento con ese ID.")
    sc.pausar()
