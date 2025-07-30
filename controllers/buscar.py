from utils.corefiles import readJson
from typing import List, Dict
import utils.screencontrollers as sc

def buscar_por_titulo() -> List[Dict]:
    sc.limpiar_pantalla()
    valor = input("Ingresa el título: ")
    archivos = ["libros.json", "musica.json", "peliculas.json"]
    resultados = []

    for archivo in archivos:
        data = readJson(archivo)
        tipo = archivo.replace(".json", "")

        for categoria, elementos in data.items():
            if isinstance(elementos, dict):
                for id_elemento, item in elementos.items():
                    if isinstance(item, dict) and "nombre" in item:
                        if valor.lower() in str(item["nombre"]).lower():
                            resultados.append({
                                "tipo": tipo,
                                "categoria": categoria,
                                "id": id_elemento,
                                "elemento": item
                            })

    if resultados:
        for r in resultados:
            print(f"[{r['tipo'].upper()} - {r['categoria']}] ID: {r['id']} -> {r['elemento']}")
            sc.pausar()
    else:
        print("No se encontraron resultados.")
        sc.pausar()

    return resultados


def buscar_por_autor() -> List[Dict]:
    sc.limpiar_pantalla()
    valor = input("Ingresa el autor, artista o director: ")
    archivos = ["libros.json", "musica.json", "peliculas.json"]
    campos = ["autor", "artista", "director"]
    resultados = []

    for archivo in archivos:
        data = readJson(archivo)
        tipo = archivo.replace(".json", "")

        for categoria, elementos in data.items():
            if isinstance(elementos, dict):
                for id_elemento, item in elementos.items():
                    if isinstance(item, dict):
                        for campo in campos:
                            if campo in item and valor.lower() in str(item[campo]).lower():
                                resultados.append({
                                    "tipo": tipo,
                                    "categoria": categoria,
                                    "id": id_elemento,
                                    "elemento": item
                                })
                                break

    if resultados:
        for r in resultados:
            print(f"[{r['tipo'].upper()} - {r['categoria']}] ID: {r['id']} -> {r['elemento']}")
            sc.pausar()
    else:
        print("No se encontraron resultados.")
        sc.pausar()

    return resultados


def buscar_por_genero() -> List[Dict]:
    sc.limpiar_pantalla()
    valor = input("Ingresa el género: ")
    archivos = ["libros.json", "musica.json", "peliculas.json"]
    resultados = []

    for archivo in archivos:
        data = readJson(archivo)
        tipo = archivo.replace(".json", "")

        for categoria, elementos in data.items():
            if isinstance(elementos, dict):
                for id_elemento, item in elementos.items():
                    if isinstance(item, dict) and "genero" in item:
                        if valor.lower() in str(item["genero"]).lower():
                            resultados.append({
                                "tipo": tipo,
                                "categoria": categoria,
                                "id": id_elemento,
                                "elemento": item
                            })

    if resultados:
        for r in resultados:
            print(f"[{r['tipo'].upper()} - {r['categoria']}] ID: {r['id']} -> {r['elemento']}")
            sc.pausar()
    else:
        print("No se encontraron resultados.")
        sc.pausar()

    return resultados

