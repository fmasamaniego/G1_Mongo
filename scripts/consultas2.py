from pymongo import MongoClient

client = MongoClient()

db = client['test']

coleccion = db['Muestras_CO2']

#1- Registros del crecimiento de CO2

consulta1 = coleccion.aggregate([
    {"$match": {'country':'Argentina', 'year': {'$gte': 2010, '$lte': 2020}}},
    {"$project": {'_id': 0, 'year': 1, 'co2_growth_prct': 1}}])


#2- Emisiones de CO2 por tipo de combustible en 2022
consulta2 = coleccion.aggregate([
    {"$match": {'year': 2022}},
    {"$project": {'coal_co2': 1, 'oil_co2': 1, 'gas_co2': 1, 'cement_co2': 1, 'flaring_co2': 1}}])

#3- Paises con mayor consumo energético per cápita y per GDP a partir del año 2000
consulta3 = coleccion.aggregate([
    {"$match": {'year': {'$gte':2000}}},
    {"$group": {'_id': '$country', 'avg_energy_per_gdp': {'$avg': '$energy_per_gdp'}, 'avg_energy_per_capita': {'$avg': '$energy_per_capita'}}},
    {"$sort": {'avg_energy_per_capita': -1}},
    {"$limit": 10},
    {"$project": {'_id': 0, 'country': '$_id', 'avg_energy_per_gdp': 1, 'avg_energy_per_capita': 1}}])

