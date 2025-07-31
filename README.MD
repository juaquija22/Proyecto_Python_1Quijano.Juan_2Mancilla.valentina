# README PROYECTO

# 🚀 Carpeta `app/` – Aplicación Principal

## 💡 Descripción del Proyecto

Esta carpeta contiene el archivo principal del proyecto: `main.py`. Aquí es donde inicia la ejecución de la aplicación, que actúa como un **administrador de colecciones** (libros, música, películas). El usuario puede agregar, ver, buscar, editar o eliminar elementos desde un menú interactivo por consola.

## 🌟 Características Destacadas

- Interfaz por consola sencilla y clara.
- Menú principal interactivo para gestionar elementos.
- Acceso organizado a las distintas funcionalidades del sistema.
- Compatibilidad con sistemas Windows, Linux y macOS.

## 🎯 Objetivo

El objetivo principal de esta parte del proyecto es proporcionar una entrada central desde donde se puede controlar todo el sistema. A través del menú, el usuario puede interactuar con los datos de manera simple y eficiente.

## 🛠 Tecnologías Utilizadas

- **Python 3**
- Módulos propios del proyecto:
  - `utils.screencontrollers` para limpiar pantalla y pausar.
  - `controllers.menu` para manejar las opciones del menú.
- Módulos estándar de Python:
  - `os`
  - `sys`

## 🗂 Estructura del Sistema

La carpeta `app/` contiene:

```
app/
└── main.py
```

### 📄 ¿Qué hace `main.py`?

- Muestra un menú con 7 opciones:
  1. Añadir un nuevo elemento
  2. Ver todos los elementos
  3. Buscar un elemento
  4. Editar un elemento
  5. Eliminar un elemento
  6. Ver elementos por categoría
  7. Salir
- Llama a funciones definidas en el módulo `menu` dentro de la carpeta `controllers/`.
- Usa funciones de la carpeta `utils/` para mantener la pantalla limpia y controlada.

------

## 📌 Notas

- El menú sigue ejecutándose hasta que el usuario elige salir.
- Cada opción está diseñada para guiar al usuario paso a paso.
- El sistema está pensado para ser fácilmente ampliable.

------

# 🌟✨ **PROYECTO PYTHON – CARPETA `controllers/`** ✨🌟

### 🎬📚🎵 Gestión de Libros, Películas y Música en Consola

------

## 📝 Descripción del Proyecto

Este sistema es una **aplicación en Python** diseñada para permitir a los usuarios **gestionar un catálogo multimedia** de manera sencilla y organizada. A través de un sistema de menús interactivos, se pueden registrar, buscar, editar, eliminar y visualizar diferentes tipos de contenido como:

- **Libros**
- **Películas**
- **Canciones**

Toda la información se guarda de forma permanente en archivos `.json`, lo cual hace que los datos persistan entre sesiones sin necesidad de bases de datos externas.

------

## 🎯 Objetivo

Crear un sistema completo de gestión de elementos multimedia que funcione desde consola, permitiendo realizar operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre datos almacenados en archivos JSON, con una interfaz amigable, validación de datos, y visualización profesional usando tablas.

------

## 💡 Características Destacadas

- ✅ **Añadir elementos multimedia** con validación (nombre, autor, género y calificación).
- 🔍 **Buscar elementos** por título, autor/artista/director o género.
- 📂 **Listar todos los elementos** organizados por tipo (libros, películas, música).
- 🛠️ **Editar** cualquier campo de un elemento ya registrado.
- 🗑️ **Eliminar** registros por nombre o ID único.
- 📊 **Visualización clara en consola** usando tablas (gracias a `tabulate`).
- 💾 **Datos persistentes** almacenados en archivos `.json` dentro de la carpeta `/data`.

------

## 🧪 Tecnologías Utilizadas

### 1. **Python 3**

Lenguaje de programación principal. Toda la lógica del sistema, incluyendo menús, interacción con el usuario, validación de datos y operaciones de archivo, está escrita en Python puro.

### 2. **Archivos `.json`**

Se usan como sistema de almacenamiento. Por ejemplo:

- `libros.json`: almacena todos los libros añadidos.
- `peliculas.json`: contiene las películas registradas.
- `musica.json`: guarda información de las canciones.

Estos archivos simulan una base de datos sencilla, legible y manipulable.

### 3. **Librería externa `tabulate`**

Una de las herramientas más importantes del sistema.
 Sirve para **mostrar los datos en consola en forma de tablas organizadas**, facilitando la lectura de la información por parte del usuario.

#### ¿Por qué es importante `tabulate`?

- Sin esta librería, la información se imprimiría como bloques desordenados de texto.
- Con `tabulate`, cada registro aparece dentro de una tabla alineada, como si fuera una hoja de Excel en la consola.

#### 📌 Ejemplo real de cómo se ve en consola:

```
+--------+------------------------+----------------------------+-------------+----------------+
|  Tipo  |         ID             |           Nombre           |   Género    |  Calificación  |
+--------+------------------------+----------------------------+-------------+----------------+
| Libro  |        1023            |   Cien años de soledad     |   Realismo  |      10/10     |
| Película |     3289            |   Interstellar             |   Ciencia Ficción |  9/10    |
| Música |       8765            |   Bohemian Rhapsody        |     Rock    |      10/10     |
+--------+------------------------+----------------------------+-------------+----------------+
```

#### 📍 ¿Dónde se usa?

Se utiliza en:

- `listar.py`: para mostrar todos los elementos por tipo.
- `buscar.py`: para mostrar los resultados de una búsqueda.
- `categoria.py`: para listar elementos filtrados por género.

------

## 🗂️ Estructura del Sistema (Carpeta `controllers/`)

Esta carpeta contiene todos los módulos funcionales del proyecto, **divididos por acción** para facilitar el mantenimiento y la organización del código:

| Módulo         | Función Principal                                            |
| -------------- | ------------------------------------------------------------ |
| `anadir.py`    | Permite agregar libros, películas o canciones al sistema. Cada elemento se almacena con un ID único y validación de los campos. |
| `buscar.py`    | Realiza búsquedas dentro de todos los archivos `.json` filtrando por título, autor o género. Muestra resultados en tabla. |
| `categoria.py` | Muestra únicamente los elementos que pertenecen a un género específico. |
| `editar.py`    | Permite modificar cualquier campo (nombre, autor, género o calificación) de un elemento existente. |
| `eliminar.py`  | Elimina elementos según su nombre o su identificador único.  |
| `listar.py`    | Lista todos los registros guardados, por tipo. Se presentan en formato de tabla para facilitar la lectura. |
| `menu.py`      | Contiene todos los menús de navegación interactiva del sistema. Desde aquí el usuario accede a cada módulo. |

------

## 📁 Estructura General del Proyecto

```
📁 proyecto/
│
├── controllers/           # Módulos principales del sistema
│   ├── anadir.py
│   ├── buscar.py
│   ├── categoria.py
│   ├── editar.py
│   ├── eliminar.py
│   ├── listar.py
│   └── menu.py
│
├── utils/                 # Funciones auxiliares
│   ├── corefiles.py       # Lectura y escritura de archivos JSON
│   ├── screencontrollers.py # Limpieza de pantalla, pausas
│   ├── validatedata.py    # Validaciones de texto y números
│
├── data/                  # Archivos de datos
│   ├── libros.json
│   ├── peliculas.json
│   └── musica.json
│
├── config.py              # Ruta base para los archivos de datos
└── main.py                # Archivo principal que ejecuta el sistema
```

------

# Proyecto de Almacenamiento de Medios en JSON

## 📖 Descripción del Proyecto

Este proyecto consiste en una estructura de datos en formato JSON que almacena información clasificada sobre libros, música y películas. Cada categoría contiene elementos con atributos como nombre, autor, género y calificación. El objetivo es proporcionar una base de datos simple y fácilmente accesible para aplicaciones educativas, de entretenimiento o de gestión multimedia.

## 🌟 Características Destacadas

- Clasificación de medios en tres categorías: libros, música y películas.
- Estructura organizada y fácil de leer en formato JSON.
- Calificación numérica para evaluar cada elemento.
- Ideal para usar en aplicaciones de recomendación o catálogos digitales.

## 🎯 Objetivo

El objetivo principal de este proyecto es ofrecer una estructura de datos sencilla para gestionar información multimedia, que pueda ser reutilizada en proyectos de desarrollo web, análisis de datos, machine learning o aprendizaje de estructuras JSON.

## 🛠 Tecnologías Utilizadas

- **JSON (JavaScript Object Notation):** para el almacenamiento estructurado de los datos.
- **Visual Studio Code (VSCode):** como editor principal (opcional).
- **Git/GitHub:** para el control de versiones y colaboración (opcional).

## 🗂 Estructura del Sistema

La carpeta principal es `data/` y contiene los siguientes archivos JSON:

```
data/
├── libros.json
├── musica.json
└── peliculas.json
```

### Contenido de cada archivo

- **libros.json**

  ```json
  {
    "libros": {
      "5339": {
        "nombre": "vale",
        "autor": "pepe",
        "genero": "chao",
        "calificacion": 10
      },
      
    }
  }
  ```

- **musica.json**

  ```json
  {
    "musica": {
      "8627": {
        "nombre": "lalala",
        "autor": "shakira",
        "genero": "reguetton",
        "calificacion": 10
      },
      
    }
  }
  ```

- **peliculas.json**

  ```json
  {
    "peliculas": {
      "4022": {
        "nombre": "avengers",
        "autor": "juan",
        "genero": "super heroes",
        "calificacion": 9
      }
    }
  }
  ```

## 📌 Notas

- Cada entrada en los archivos está indexada por un ID único.
- La estructura es fácilmente escalable para incluir más campos o categorías.

------



# 🔧 Carpeta `utils/` – Funciones de Utilidad del Proyecto

## 💡 Descripción del Proyecto

La carpeta `utils` contiene funciones clave que ayudan a manejar tareas comunes dentro del proyecto, como manipular archivos JSON, validar datos ingresados por el usuario y controlar la pantalla en consola. Todo está organizado por módulos para mantener el código limpio y reutilizable.

## 🌟 Características destacadas

- Lectura, escritura, actualización y eliminación de archivos JSON.
- Validación de entradas de texto, enteros y flotantes.
- Funciones para limpiar la consola y pausar la ejecución, adaptadas a cualquier sistema operativo.

## 🎯 Objetivo

El objetivo de esta carpeta es reunir herramientas útiles que pueden ser llamadas desde otras partes del proyecto, evitando repetir código y facilitando el mantenimiento general del sistema.

## 🛠 Tecnologías Utilizadas

- **Python 3**
- Módulos estándar:
  - `json`
  - `os`
  - `sys`
  - `typing`

## 🗂 Estructura del Sistema

La carpeta `utils/` contiene los siguientes archivos:

```
utils/
├── corefiles.py
├── screencontrollers.py
└── validatedata.py
```

### 📄 Descripción de los Archivos

- **`corefiles.py`**
   Funciones para trabajar con archivos JSON:
  - `readJson()` – Lee y carga el contenido de un archivo JSON.
  - `writeJson()` – Guarda datos en formato JSON.
  - `updateJson()` – Permite modificar datos existentes o insertar nuevos.
  - `deleteJson()` – Elimina información específica dentro del archivo.
  - `initializeJson()` – Crea un archivo JSON con una estructura base si no existe.
- **`screencontrollers.py`**
   Funciones para interactuar con la consola:
  - `pausar()` – Pausa la ejecución hasta que el usuario presione ENTER.
  - `limpiar_pantalla()` – Limpia la pantalla, compatible con Windows, Linux y macOS.
- **`validatedata.py`**
   Validaciones de entrada de datos:
  - `validateInt()` – Asegura que el usuario ingrese un número entero válido.
  - `validatetext()` – Verifica que el texto contenga solo letras y espacios.
  - `validateflot()` – Intenta leer un número flotante (nota: actualmente retorna un string, podría mejorarse para convertir a `float`).

------

## 📝 Notas

- Estas funciones están listas para ser usadas desde cualquier parte del proyecto.
- Puedes seguir ampliando los validadores o las herramientas según lo necesites.

------

# ⚙️ Archivo `config.py` – Configuración del Proyecto

## 💡 Descripción del Proyecto

Este archivo contiene una configuración básica pero fundamental para el funcionamiento del sistema: define la ruta donde se encuentran los archivos de datos (libros, música y películas). Centralizar esta información facilita cambios futuros y mejora la mantenibilidad del código.

## 🌟 Características Destacadas

- Define una constante global `DB_PATH`.
- Evita escribir rutas manualmente en distintos archivos del proyecto.
- Facilita la adaptación del sistema si se cambia la ubicación de los datos.

## 🎯 Objetivo

El objetivo de este archivo es actuar como punto central para almacenar rutas o configuraciones básicas que otros módulos del proyecto pueden necesitar. Esto ayuda a mantener el código limpio, más organizado y más fácil de modificar si es necesario.

## 🛠 Tecnologías Utilizadas

- **Python 3**
- Módulo estándar (sin dependencias externas)

## 🗂 Estructura del Archivo

```
config.py
```

### Contenido actual:

```python
DB_PATH = "data/"
```

- `DB_PATH` indica que los archivos JSON que contienen los datos del proyecto están ubicados en la carpeta `data/`.

------

## 📌 Notas

- Si en algún momento decides mover tus archivos de datos a otra carpeta, solo necesitas actualizar esta línea, y el cambio se aplicará automáticamente en todos los módulos que usen `DB_PATH`.

------

## ✍️ Autores

 Valentina Mancilla Casanova y Juan pablo Quijano Martinez 



