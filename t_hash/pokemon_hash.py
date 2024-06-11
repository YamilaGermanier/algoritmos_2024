"""
Escribir un algoritmo que permita utilizar tres tablas hash para guardar los datos de Pokémons,
que contemple las siguientes actividades: 
    a. en la primera tabla hash la función hash debe ser sobre el tipo de Pokémon, en la segunda
tabla la función hash deberá utilizar el ultimo dígito del número del Pokémon como clave y 
la tercera sera en base  a su nivel repartiéndolos en 10 posiciones dentro de la tabla; 
    b. debe utilizar tablas hash abiertas con listas como estructura secundaria;
    c. si el Pokémon es de más de un tipo deberá cargarlo en cada uno de las tabla que indiquen estos tipos;
    d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
    e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
    f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
    g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
"""

"""
pokemons = [ {'número': 1,'nombre': "Bulbasaur", 'tipo': "Planta", 'subtipo': "Veneno", 'nivel': 10},
            {'número': 4,'nombre': "Charmander", 'tipo': "Fuego", 'subtipo': "", 'nivel': 10},
            {'número': 6,'nombre': "Charizard", 'tipo': "Fuego", 'subtipo': "Volador", 'nivel': 55},
            {'número': 7,'nombre': "Squirtle", 'tipo': "Agua", 'subtipo': "", 'nivel': 10},
            {'número': 10,'nombre': "Caterpie", 'tipo': "Insecto", 'subtipo': "", 'nivel': 5},
            {'número': 16,'nombre': "Pidgey", 'tipo': "Normal", 'subtipo': "Volador", 'nivel': 5},
            {'número': 19,'nombre': "Ratata", 'tipo': "Normal", 'subtipo': "", 'nivel': 5},
            {'número': 25,'nombre': "Pikachu", 'tipo': "Eléctrico", 'subtipo': "", 'nivel': 15},
            {'número': 27,'nombre': "Sandshrew", 'tipo': "Tierra", 'subtipo': "", 'nivel': 15},
            {'número': 39,'nombre': "Mankey", 'tipo': "Pelea", 'subtipo': "", 'nivel': 10},
            {'número': 56,'nombre': "Pidgey", 'tipo': "Normal", 'subtipo': "Volador", 'nivel': 25},
            {'número': 63,'nombre': "Abra", 'tipo': "Psíquico", 'subtipo': "", 'nivel': 35},
            {'número': 76,'nombre': "Golem", 'tipo': "Roca", 'subtipo': "Tierra", 'nivel': 35},
            {'número': 81,'nombre': "Magnemite", 'tipo': "Eléctrico", 'subtipo': "Acero", 'nivel': 35},
            {'número': 92,'nombre': "Gastly", 'tipo': "Fantasma", 'subtipo': "Veneno", 'nivel': 25},
            {'número': 124,'nombre': "Jynx", 'tipo': "Hielo", 'subtipo': "Psíquico", 'nivel': 35},
            {'número': 131,'nombre': "Lapras", 'tipo': "Agua", 'subtipo': "Hielo", 'nivel': 30},
            {'número': 132,'nombre': "Ditto", 'tipo': "Normal", 'subtipo': "", 'nivel': 10},
            {'número': 133,'nombre': "Eevee", 'tipo': "Normal", 'subtipo': "", 'nivel': 15},
            {'número': 135,'nombre': "Jolteon", 'tipo': "Eléctrico", 'subtipo': "", 'nivel': 45},
            {'número': 143,'nombre': "Snorlax", 'tipo': "Normal", 'subtipo': "", 'nivel': 45},
            {'número': 147,'nombre': "Dratini", 'tipo': "Dragón", 'subtipo': "", 'nivel': 15},
            {'número': 149,'nombre': "Dragonite", 'tipo': "Dragón", 'subtipo': "Volador", 'nivel': 45},
            {'número': 150,'nombre': "Mewto", 'tipo': "Psíquico", 'subtipo': "", 'nivel': 90},
]
"""


# número, nombre, tipo, subtipo, nivel
pokemons = [ {'número': 1,'nombre': "Bulbasaur", 'tipo': ["Planta", "Veneno"], 'nivel': 10},
            {'número': 4,'nombre': "Charmander", 'tipo': ["Fuego"], 'nivel': 10},
            {'número': 6,'nombre': "Charizard", 'tipo': ["Fuego", "Volador"], 'nivel': 55},
            {'número': 7,'nombre': "Squirtle", 'tipo': ["Agua"], 'nivel': 10},
            {'número': 10,'nombre': "Caterpie", 'tipo': ["Insecto"], 'nivel': 5},
            {'número': 16,'nombre': "Pidgey", 'tipo': ["Normal", "Volador"], 'nivel': 5},
            {'número': 19,'nombre': "Ratata", 'tipo': ["Normal"], 'nivel': 5},
            {'número': 25,'nombre': "Pikachu", 'tipo': ["Eléctrico"], 'nivel': 15},
            {'número': 27,'nombre': "Sandshrew", 'tipo': ["Tierra"], 'nivel': 15},
            {'número': 39,'nombre': "Mankey", 'tipo': ["Pelea"], 'nivel': 10},
            {'número': 56,'nombre': "Pidgey", 'tipo': ["Normal", "Volador"], 'nivel': 25},
            {'número': 63,'nombre': "Abra", 'tipo': ["Psíquico"], 'nivel': 35},
            {'número': 76,'nombre': "Golem", 'tipo': ["Roca", "Tierra"], 'nivel': 35},
            {'número': 81,'nombre': "Magnemite", 'tipo': ["Eléctrico", "Acero"], 'nivel': 35},
            {'número': 92,'nombre': "Gastly", 'tipo':[ "Fantasma", "Veneno"], 'nivel': 25},
            {'número': 124,'nombre': "Jynx", 'tipo': ["Hielo", "Psíquico"], 'nivel': 35},
            {'número': 131,'nombre': "Lapras", 'tipo': ["Agua", "Hielo"], 'nivel': 30},
            {'número': 132,'nombre': "Ditto", 'tipo': ["Normal"], 'nivel': 10},
            {'número': 133,'nombre': "Eevee", 'tipo': ["Normal"], 'nivel': 15},
            {'número': 135,'nombre': "Jolteon", 'tipo': ["Eléctrico"], 'nivel': 45},
            {'número': 143,'nombre': "Snorlax", 'tipo': ["Normal"], 'nivel': 45},
            {'número': 147,'nombre': "Dratini", 'tipo': ["Dragón"], 'nivel': 15},
            {'número': 149,'nombre': "Dragonite", 'tipo': ["Dragón", "Volador"], 'nivel': 45},
            {'número': 150,'nombre': "Mewto", 'tipo': ["Psíquico"], 'nivel': 90},
]


pokemons_por_tipo = {}
pokemons_por_subtipo = {}
pokemons_por_digito = {}
pokemons_por_nivel = {}


print("--------------")

# A__ 1era-- tipo de pokémon 
def hash_tipo(pokemon):
    return pokemon['tipo'][0]
# le agregué el subtipo 
def hash_subtipo(pokemon):
    if len(pokemon['tipo']) > 1:
        return pokemon['tipo'][1]  


# A__ 2era-- último dígito del número de pokémon
def hash_num(pokemon):
    return pokemon['número']%10


##A__ 3era-- nivel
def hash_nivel(pokemon):
    return pokemon['nivel']//10



###################################################3
for pokemon in pokemons:
    tipo = hash_tipo(pokemon)
    if tipo not in pokemons_por_tipo:
        pokemons_por_tipo[tipo]= []
    pokemons_por_tipo[tipo].append(pokemon)
    #print(f"Pokémon añadido a {tipo}: {pokemon}")


    subtipo=hash_subtipo(pokemon)
    if subtipo:
        if subtipo not in pokemons_por_subtipo:
            pokemons_por_subtipo[subtipo] = []
        pokemons_por_subtipo[subtipo].append(pokemon)
    

    ######
    clave = hash_num(pokemon)
    if clave not in pokemons_por_digito:
        pokemons_por_digito[clave]= []
    pokemons_por_digito[clave].append(pokemon)


    ######
    nivel = hash_nivel(pokemon)
    if nivel not in pokemons_por_nivel:
         pokemons_por_nivel[nivel] = []
    pokemons_por_nivel[nivel].append(pokemon)


#print(pokemons_por_tipo)   FUNCIONA, ARMA LAS TABLAS
# Para imprimir más lindo:
for tipo, pokemon_tipo in pokemons_por_tipo.items():
    print(f"Tipo: {tipo}")
    for pokemon in pokemon_tipo:
            print(f"  {pokemon['nombre']}")

    print("--------------")

print(pokemons_por_subtipo)
print("---------------------------------------------------------------------------------------------------")
for subtipo, pokemon_subtipo in pokemons_por_subtipo.items():
    print(f"Subtipo: {subtipo}")
    for pokemon in pokemon_subtipo:
            print(f"  {pokemon['nombre']}")

    print("--------------")


print(pokemons_por_digito)
print("---------------------------------------------------------------------------------------------------")

print("---------------------------------------------------------------------------------------------------")
for nivel, pokemon_nivel in pokemons_por_nivel.items():
    print(f"Nivel: {nivel}")
    for pokemon in pokemon_nivel:
            print(f"  {pokemon['nombre']}")

    print("--------------")