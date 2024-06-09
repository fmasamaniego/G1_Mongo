#Para realizar consultas en la base de datos de MongoDB

from pymongo import MongoClient
import json


# Conexión al servidor local de MongoDB
client = MongoClient('localhost', 27017)

# Conexión a la base de datos
db = client['test']

# Conexión a la colección
collection = db['Muestras_CO2']

#Realizar consultas

#1- Todos los registros de Argentina

documents_arg = collection.find({"country": "Argentina"})


#Guardar los datos en un archivo json
data_arg = []
for document in documents_arg:
    document['_id'] = str(document['_id'])
    data_arg.append(document)

with open('./datos_argentina.json', 'w') as f:
    json.dump(data_arg, f, indent=4)

#2- Todos los registros de Argentina a partir del año 2000
documents_arg_2000 = collection.find({"country": "Argentina", "year": {"$gte": "2000"}})
data_arg_2000 = []
for document in documents_arg_2000:
    document['_id'] = str(document['_id'])
    data_arg_2000.append(document)

with open('./datos_argentina_2000.json', 'w') as f:
    json.dump(data_arg_2000, f, indent=4)


#3- Paises con mayor emisión de C02 en un año específico
top_co2_countries = collection.find({"year": "2020", "co2": {"$ne": ""}}).sort("co2", -1).limit(10)

data_top_co2_countries_year = []
for document in top_co2_countries:
    document['_id'] = str(document['_id'])
    data_top_co2_countries_year.append(document)

with open('./top_co2_countries_year.json', 'w') as f:
    json.dump(data_top_co2_countries_year, f, indent=4)


#4- Paises con mayor crecimiento de emisión de C02 en un rango de años
countries_co2_growth = collection.aggregate([
    {"$match": {"year": {"$gte": "2000"}}},
    {"$group": {"_id": "$country", "co2_growth": {"$sum": "$co2_growth_abs"}}},
    {"$sort": {"co2_growth": -1}},
    {"$limit": 10}
])

data_top_co2_growth = []

for document in countries_co2_growth:
    document['_id'] = str(document['_id'])
    data_top_co2_growth.append(document)

with open('./top_co2_growth.json', 'w') as f:
    json.dump(data_top_co2_growth, f, indent=4)
 
