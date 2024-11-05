"""
1. Se tiene datos de los Pokémons de las 8 generaciones cargados de manera desordenadade los cuales se conoce su nombre, número, tipo/tipos para el cual debemos construir tres árboles para acceder de manera eficiente a los datos, contemplando lo siguiente: 
    a) los índices de cada uno de los árboles deben ser nombre, número y tipo; 
    b) mostrar todos los datos de un Pokémon a partir de su número y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–; 
    c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico; 
    d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre; 
    e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum; f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
"""

from arbol_avl import BinaryTree

# nombre - numero - tipo
listaPokemons = [
    {"nombre": "Bulbasaur", "numero": 1, "tipo": ["Planta", "Veneno"]},
    {"nombre": "Totodile", "numero": 158, "tipo": ["Agua"]},
    {"nombre": "Breloom", "numero": 286, "tipo": ["Planta", "Lucha"]},
    {"nombre": "Lucario", "numero": 448, "tipo": ["Lucha", "Acero"]},
    {"nombre": "Axew", "numero": 610, "tipo": ["Dragón"]},
    {"nombre": "Froakie", "numero": 656, "tipo": ["Agua"]},
    {"nombre": "Rockruff", "numero": 744, "tipo": ["Roca"]},
    {"nombre": "Sobble", "numero": 816, "tipo": ["Agua"]},
    {"nombre": "Yamper", "numero": 835, "tipo": ["Eléctrico"]},
    {"nombre": "Wooloo", "numero": 831, "tipo": ["Normal"]},
    { 'nombre': 'Jolteon', 'numero': 135, 'tipo': ['Eléctrico'] },
    { 'nombre': 'Lycanroc', 'numero': 745, 'tipo': ['Roca'] },
    { 'nombre': 'Tyrantrum', 'numero': 697, 'tipo': ['Roca', 'Dragón'] }
]

arbol_nombre=BinaryTree()
arbol_numero=BinaryTree()
arbol_tipo=BinaryTree()

######## a) los índices de cada uno de los árboles deben ser nombre, número y tipo;
for pokemon in listaPokemons:
    arbol_nombre.insert_node(pokemon["nombre"], pokemon)
    arbol_numero.insert_node(pokemon["numero"], pokemon)
    arbol_tipo.insert_node(pokemon["tipo"], pokemon)

#arbol_nombre.inorden()
#arbol_numero.inorden()
#arbol_tipo.inorden()

"""for pokemon in listaPokemons:
    arbol.insert_node (pokemon['nombre'], pokemon)
arbol.inorden()
"""

print(" ")
print("----------------")

######  b) mostrar todos los datos de un Pokémon a partir de su número ;
num= int(input("Ingrese el número del pokémon a buscar: "))
pos=arbol_numero.search(num)
if pos is not None:
    print(pos.value, pos.other_value)  
else:
    print("No se encontro el pokémon con ese número")
print("")

# y nombre –para este último, la búsqueda debe ser por proximidad, es decir si busco “bul” se deben mostrar todos los Pokémons cuyos nombres comiencen o contengan dichos caracteres–
buscado = input("Ingrese el nombre del pokémon a buscar: ")
arbol_nombre.buscar_por_coincidencia(buscado) # ya retorno el dato

print(" ")
print("----------------")

# c) mostrar todos los nombres de todos los Pokémons de un determinado tipo agua, fuego, planta y eléctrico;
print("Pokémons del tipo Agua: ")
arbol_tipo.mostrar_por_tipo("Agua")
print("")
print("Pokémons del tipo Fuego: ")
arbol_tipo.mostrar_por_tipo("Fuego")
print("")
print("Pokémons del tipo Planta: ")
arbol_tipo.mostrar_por_tipo("Planta")
print("")
print("Pokémons del tipo Eléctrico: ")
arbol_tipo.mostrar_por_tipo("Électrico")
print("")
print(" ")
print("----------------")


# d) realizar un listado en orden ascendente por número y nombre de Pokémon, y además un listado por nivel por nombre; 
print("Listado por número")
arbol_numero.listar_por_numero()
print(" ")
print("Listado por nivel")
arbol_nombre.by_level()

print(" ")
print("----------------")

#   e) mostrar todos los datos de los Pokémons: Jolteon, Lycanroc y Tyrantrum; 
print('Pokemones buscados')
print(arbol_nombre.search('Lycanroc').other_value)
print(arbol_nombre.search('Tyrantrum').other_value)
print(arbol_nombre.search('Jolteon').other_value)

print(" ")
print("----------------")

# f) Determina cuantos Pokémons hay de tipo eléctrico y acero. 
print("El número de Pokémons de tipo Eléctrico es de: ", arbol_tipo.contar_por_tipo("Eléctrico"))
print("El número de Pokémons de tipo Acero es de: ", arbol_tipo.contar_por_tipo("Acero"))

print(" ")
print("----------------")