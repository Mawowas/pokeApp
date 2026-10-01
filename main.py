
# cadena de evolucion https://pokeapi.co/api/v2/pokemon-species/{id_o_nombre}/

import requests 

class PokemonNoEncontrado(Exception):
    pass

# PEDIDO Y REVISION DEL POKEMON ---------
poke_nombre = input("ingresar pokemon: ")
URL = "https://pokeapi.co/api/v2/pokemon/" + poke_nombre
codigo = requests.get(URL)

if codigo.status_code != 200:
    raise PokemonNoEncontrado(f"Pokemon: {poke_nombre}, No encontrado")
try:
    datos = codigo.json()   
except PokemonNoEncontrado:
    print(f"ERROR POKEMON: '{poke_nombre}', NO ENCONTRADO")
# ----------------------------------


#   ADMINISTRACION DE DATOS DEL POKEMON
# ----------------------------------
id_pokemon = str(datos['id'])
url_especie = 'https://pokeapi.co/api/v2/pokemon-species/' + id_pokemon
codigo_url_especie = requests.get(url_especie)
datos_especie = codigo_url_especie.json()
url_cadena_especie = requests.get(datos_especie["evolution_chain"]["url"])
datos_cadena_especie = url_cadena_especie.json()
# ----------------------------------

#   Muestra de datos ------------------
print("\nTipo:")
for type in datos['types']:
    print(type['type']['name'])

print()

print(f"Lista de Movimientos de {poke_nombre}:")
for i, movimientos in enumerate(datos["moves"], start= 1):

    if i % 5 != 0:
        print(movimientos["move"]["name"], end=" -- ")
    else:
        print(movimientos["move"]["name"])

# nivel_minimo = datos_cadena_especie["chain"]["evolves_to"][0]["evolution_details"][0]["min_level"]
# objeto_necesario = datos_cadena_especie["chain"]["evolves_to"][0]["evolves_to"][0]["evolution_details"][0]["item"]["name"]
# print()

usa_item = datos_cadena_especie["chain"]["evolves_to"][0]["evolves_to"][0]["evolution_details"][0]["item"]



print()
print("Requisitos de Evolucion: ")
print("nivel minimo: ", datos_cadena_especie["chain"]["evolves_to"][0]["evolution_details"][0]["min_level"])

if usa_item != None:
    # print("Objeto: ", datos_cadena_especie["chain"]["evolves_to"][0]["evolves_to"][0]["evolution_details"][0]["item"]["name"])
    print("Objeto: ", usa_item["name"])

#print(f'ID: {id_pokemon} {url_cadena}')


# LINK DE EVOLUCION DE PIKACHU https://pokeapi.co/api/v2/evolution-chain/10/
# ABAJO DICE QUE EVOLUCIONA RAICHU