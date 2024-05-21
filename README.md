
# Bases de datos orientadas a documentos

Técnicas y Herramientas de Datos Masivos - T.U.P.E.D


Grupo 1:



Armú Yamil

Colignon Sabrina

Samaniego Francisco


## Índice

1. [Introducción](#introducción)
2. [Cómo crear una BD](#cómo-crear-una-bd)
3. [Pymongo: trabajar con Python](#pymongo-trabajar-con-python)
4. [Lenguaje de consultas: MQL](#lenguaje-de-consulta-mql)
5. [Código de interés](#código-de-interés)



## Introducción

Las bases de datos orientadas a documentos son un tipo de base de datos NoSQL que se centra en trabajar con archivos de tipo JSON
[Bibliografía](https://drive.google.com/file/d/1UduiSCH72_og31DYwMwSHLNX8kxrztAL/view?usp=sharing
)

### Herramienta: MongoDB

MongoDB es una base de datos de código abierto especializada en trabajar con documentos.
[¿Qué es MongoDB?](https://www.mongodb.com/es/company/what-is-mongodb#:~:text=MongoDB%20es%20una%20base%20de%20datos%20de%20documentos,como%20un%20modelo%20de%20consultas%20e%20indexaci%C3%B3n%20avanzado.)

### Instalación
Para poder trabajar con mongoDB es necesario instalar el servicio y además el gestor o GUI conocido como mongoDB Compass
[Instalar MongoDB](https://www.mongodb.com/try/download/community)



## Cómo crear una BD

### Creación
Una vez instalada mongoDB Compass pueden crearse bases de datos desde 0.

Para esto es necesario recordar que una base de datos está definida como un conjunto de colecciones y que cada colección es un conjunto de documentos.

### Ejemplo:

1. Asignar un nombre a una base de datos --> "pruebas"
2. Crear una colección dentro de la BD ---> "alumnos"
3. En la consola de la herramienta cambiar a la BD creada 


``` 
use pruebas

```
4. Realizar la operación deseada, por ejemplo guardar un documento
```
db.alumnos.insertOne({
    'nombre' : 'Francisco',
    'apellido': 'Samaniego',
    'edad': 26,
    'residencia': 'Paraná',
    'tiene_hermanos': True,
    'vecino': 'Sabrina'
})
```



## Pymongo: trabajar con Python

### ¿Qué es Pymongo?

Pymongo es un framework que contiene herramientas para poder trabajar con Mongo desde Python.
[Documentación](https://pymongo.readthedocs.io/en/stable/index.html)

### ¿Cómo trabajar con Pymongo?

Para trabajar con esta librería necesario tenerla instalada 
```
pip install pymongo
```

Luego en un script de Python se deben realizar las conexiones correspondientes
[Script de conexión](https://github.com/fmasamaniego/G1_Mongo/blob/main/scripts/conexion_mongodb.py)

## Lenguaje de consulta MQL
Mongo Query Lenguage es el conjunto de sintaxis utilizado para realizar consulta en una base de datos

Si bien existen dos funciones principales encargadas en encontrar documentos:

find: encontrar un archivo o archivos con una característica indicada.

Para trabajar con esta función existen operadores de consulta
[Operadores de consulta](https://www.w3schools.com/mongodb/mongodb_query_operators.php)

aggregate: realizar un conjunto de operaciones de agregación para encontrar documentos


Las funciones de agregación permiten agrupar, ordenar, realizar operaciones matemáticas y muchas operaciones mas, utilizando sus propios operadores
[Operadores de agregación](https://www.w3schools.com/mongodb/mongodb_aggregations_intro.php)

## Código y links de interés
En esta sección se encuentran los links a los scripts contenidos en el repositorio

### Conjunto de datos utilizado para el trabajo
[Muestras de CO2 por país](https://github.com/owid/co2-data/blob/master/README.md)

### Crear un archivo json a partir de un archivo csv
[Crear json usando csv](https://github.com/fmasamaniego/G1_Mongo/blob/main/scripts/import_csv.py)

### Crear una base de datos de una sola colección
[BD de una sola colección](https://github.com/fmasamaniego/G1_Mongo/blob/main/scripts/una_coleccion_pymongo.py)

### Crear una base de datos con varias colecciones
[BD de varias colecciones](https://github.com/fmasamaniego/G1_Mongo/blob/main/scripts/varias_colecciones_pymongo.py)
