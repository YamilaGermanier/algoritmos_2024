"""
Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: nombre, cantidad
de torneos ganados, cantidad de batallas perdidas y cantidad de batallas ganadas. Y además
la lista de sus Pokémons, de los cuales se sabe: nombre, nivel, tipo y subtipo. Se pide resolver
las siguientes actividades utilizando lista de lista implementando las funciones necesarias:

    a. obtener la cantidad de Pokémons de un determinado entrenador;
    b. listar los entrenadores que hayan ganado más de tres torneos;
    c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
    d. mostrar todos los datos de un entrenador y sus Pokémos;
    e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
    f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
    (tipo y subtipo);
    g. el promedio de nivel de los Pokémons de un determinado entrenador;
    h. determinar cuántos entrenadores tienen a un determinado Pokémon;
    i. mostrar los entrenadores que tienen Pokémons repetidos;
    j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
    o Wingull;
    k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
    como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
    deberán mostrar los datos de ambos;
"""

from random import choice
from lista_ejemplo import show_list_list, by_name, search
from entrenadores import entrenadores
from pokemons import pokemons


names = ["Ash Ketchum", "Goh", "Leon", "Chloe", "Raihan"]

lista_entrenadores = []

for entrenador in entrenadores:
    entrenador.update({'sublist': []})
    lista_entrenadores.append(entrenador)

for pokemon in pokemons:
    pos = search(lista_entrenadores, 'nombre', choice(names))
    if pos is not None:
        lista_entrenadores[pos]['sublist'].append(pokemon)
    else:
        print('no existe el entrenador')

lista_entrenadores.sort(key=by_name)
show_list_list('Entrenadores', 'Pokemons', lista_entrenadores)

print("-----------------------------------------------------------")

#  a. obtener la cantidad de Pokémons de un determinado entrenador;
x= input("Ingrese el entrenador a buscar: ")
for entrenador in lista_entrenadores:
    if entrenador['nombre'] == x:
        print("Tiene ", len(entrenador['sublist']), " pokémons.")

print("-----------------------------------------------------------")

#  b. listar los entrenadores que hayan ganado más de tres torneos;
print("Entrenadores con más de tres torneos ganados: ")
for entrenador in lista_entrenadores:
    if entrenador['torneos_ganados']>3:
        print("- ", entrenador['nombre'])

print("-----------------------------------------------------------")

#  c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados; LAMBDA argumentos : expresión
winner = max(lista_entrenadores, key=lambda entrenador: entrenador['torneos_ganados'])
print("El entrenador con más torneos ganados: ", winner['nombre'])
poke_winner = winner['sublist']
if poke_winner is not []:
    bestP = max(poke_winner, key=lambda pokemon: pokemon['nivel'])
    print("Su pokemon más fuerte: ", bestP['nombre'])
else:
    print("El entrenador no tiene pokémons") # salvando en teoría ValueError: max() arg is an empty sequence

print("-----------------------------------------------------------")

#  d. mostrar todos los datos de un entrenador y sus Pokémos;
buscado= input("Ingrese el entrenador que desea buscar: ")
for entrenador in lista_entrenadores:
    if buscado == entrenador['nombre']:
        print(entrenador)

print("-----------------------------------------------------------")

#  e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
list_mejores=[]
for entrenador in lista_entrenadores:
    lost=entrenador['batallas_perdidas']
    win=entrenador['batallas_ganadas']
    total=lost+win
    if (win*100)/total > 79:
        list_mejores.append(entrenador)

print("Entrenadores cuyo porcentaje de batallas ganados es mayor al 79 %: ")
for entrenador in list_mejores:
    print(entrenador['nombre'])

print("-----------------------------------------------------------")

#  f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador
#  (tipo y subtipo);
for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if 'Fuego' in pokemon['tipo'] and 'Planta' in pokemon['tipo']:
            print("Pokemons de tipo fuego y planta: ", pokemon)
        elif pokemon['subtipo']is not None and 'Agua' in pokemon['tipo'] and 'Volador' in pokemon['subtipo']:
            print("Pokemon de tipo agua/volador: " , pokemon)

print("-----------------------------------------------------------")

#  g. el promedio de nivel de los Pokémons de un determinado entrenador;
x=input("Ingrese el entrenador: ")
cont=0
nivel=0
for entrenador in lista_entrenadores:
    if entrenador['nombre'] == x:
        for pokemon in entrenador['sublist']:
            cont+=1
            nivel+=pokemon['nivel']
promedioNivel=nivel/cont
print(f"El promedio de nivel de los pokémons del entrenador {x} es {promedioNivel}")        

print("-----------------------------------------------------------")

#  h. determinar cuántos entrenadores tienen a un determinado Pokémon;
x=input("Ingrese el pokémon a buscar: ")
trainer=0
list_aux=[]
for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['nombre'] == x:
            trainer+=1
            list_aux.append(entrenador)

print(f"Los entrenadores que tienen al pokémon {x} son {trainer}: ")
for e in list_aux:
    print(e['nombre'])

print("-----------------------------------------------------------")

#  i. mostrar los entrenadores que tienen Pokémons repetidos;
entrenadores_con_repetidos = []

for entrenador in lista_entrenadores:
    nombres_pokemons = [pokemon['nombre'] for pokemon in entrenador['sublist']]
    nombres_vistos = []
    repetidos = False
    
    for nombre in nombres_pokemons:
        if nombre in nombres_vistos:
            repetidos = True
            break
        else:
            nombres_vistos.append(nombre)
    
    if repetidos:
        entrenadores_con_repetidos.append(entrenador['nombre'])

print("Entrenadores que tienen Pokémons repetidos: ")
for nombre in entrenadores_con_repetidos:
    print(nombre)

print("-----------------------------------------------------------")
            

#  j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion
#    o Wingull;
list_j=[]
for entrenador in lista_entrenadores:
    for pokemon in entrenador['sublist']:
        if pokemon['nombre'] == 'Terrakion' or pokemon['nombre'] == 'Tyrantrum' or pokemon['nombre'] == 'Wingull':
            list_j.append(entrenador['nombre'])   
print("Entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull")
for e in list_j:            
    print(e)

print("-----------------------------------------------------------")

#  k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
#   como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
#   deberán mostrar los datos de ambos;
print("Búsqueda:")
x=input("Ingrese el nombre entrenador a buscar: ")
y=input("Ingrese el nombre del pokémon a buscar: ")
for entrenador in lista_entrenadores:
    if entrenador['nombre'] == x:
        for pokemon in entrenador['sublist']:
            if pokemon['nombre']== y:
                print("Datos del entrenador: ",entrenador)
                print("Datos del pokémon: ",pokemon)
                
