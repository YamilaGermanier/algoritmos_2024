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
"""
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
"""

print("---------------------------------------------------------------------------------------------------")
print("---------------------------------------------------------------------------------------------------")

# d. deberá permitir cargar Pokémons de los cuales se dispone de su número, nombre, tipo/s, nivel.
def cargar_pokemon(numero, nombre, tipo, nivel):
    nuevo_pokemon = {'número': numero, 'nombre': nombre, 'tipo': tipo, 'nivel': nivel}
    pokemons.append(nuevo_pokemon)

cargar_pokemon(151, "Mew", ["Psíquico"], 90)

print("---------------------------------------------------------------------------------------------------")

# e. mostrar todos los Pokémons cuyos numeros terminan en 3, 7 y 9;
print("Pokémons cuyos numeros terminan en 3, 7 y 9:")
for pokemon in pokemons:
    if pokemon['número'] % 10 in [3, 7, 9]:
        print(f"{pokemon['nombre']} (#{pokemon['número']})")

print("---------------------------------------------------------------------------------------------------")

# f. mostrar todos los Pokémons cuyos niveles son multiplos de 2, 5 y 10;
def mostrar_niveles_multiplos(pokemons, multiplos):
    for pokemon in pokemons:
        if pokemon['nivel'] % multiplos == 0:
            print(f"{pokemon['nombre']} (Nivel {pokemon['nivel']})")

print("Pokémons cuyos niveles son multiplos de 2:")
mostrar_niveles_multiplos(pokemons, 2)
print("--------------")
print("Pokémons cuyos niveles son multiplos de 5:")
mostrar_niveles_multiplos(pokemons, 5)
print("--------------")
print("Pokémons cuyos niveles son multiplos de 10:")
mostrar_niveles_multiplos(pokemons, 10)  # Múltiplos de 10
print("--------------")
print("---------------------------------------------------------------------------------------------------")

# g. mostrar todos los Pokémons de los siguientes tipo: Acero, Fuego, Electrifico, Hielo
tipos_buscados = ["Acero", "Fuego", "Eléctrico", "Hielo"]

print("Pokémons de tipo Acero, Fuego, Eléctrico, Hielo:")  
for tipo in tipos_buscados:
    if tipo in pokemons_por_tipo:
        for pokemon in pokemons_por_tipo[tipo]:
            print(pokemon)
