"""
24. Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:
    a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posición
uno la cima de la pila;
    b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
la cantidad de películas en la que aparece;
    c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
    d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
"""
# https://m.imdb.com/list/ls044111840/ Personajes y sus pelis

from tp2_pila import Stack

mcu = Stack()
pila_aux = Stack()

"""personajes = [['Iron-Man','10'], ['Captain America','9'], ['Black Widow','9'], ['Thor','8'], 
              ['Hawkeye','5'], ['Nick Fury','11'], ['Agent Coulson','5'], ['Jane Foster','4'], 
              ['Gamora','5'], ['Rocket Raccoon', '6'],['Groot','6'], ['Yelena Belova', '1'],
              ['Dr Strange', '6'], ['Monica Rambeau', '2'], ['Hela', '1']]"""

personajes = [
    {'nombre':'Iron-Man',
     'apariciones':10 },
    {'nombre':'Captain America',
     'apariciones':9},
    {'nombre':'Black Widow',
     'apariciones':9},
    {'nombre':'Thor',
     'apariciones':8},
    {'nombre':'Hawkeye',
    'apariciones':5},
    {'nombre':'Nick Fury',
    'apariciones':11},
    {'nombre':'Agent Coulson',
    'apariciones':5},
    {'nombre':'Jane Foster',
     'apariciones':4},
    {'nombre':'Gamora',
     'apariciones':5},
    {'nombre':'Rocket Raccoon',
     'apariciones':6},
    {'nombre':'Groot',
     'apariciones':6},
    {'nombre':'Yelena Belova',
     'apariciones':1},
    {'nombre':'Dr. Strange',
     'apariciones': 6},
    {'nombre':'Monica Rambeau',
     'apariciones':2},
    {'nombre':'Hela',
     'apariciones':1}
]


for personaje in personajes:
    mcu.push(personaje)

# print(mcu.on_top()) # control
print("---------------------------------------------------------")
#### a. determinar posición de Rocket y Groot
posicion=1
while mcu.size()>0:
    # print(mcu.pop()['nombre']) # probando si funca
    personaje=mcu.pop() # variable para seguir trabajando sin volver a llamar a .pop()
    if(personaje['nombre'] == 'Rocket Raccoon' or personaje['nombre'] == 'Groot'):
        print(personaje['nombre'], 'está en la posicion', posicion)
    posicion+=1
    pila_aux.push(personaje)



### b. determinar los personajes que participaron en más de 5 películas de la saga, además indicar
###    la cantidad de películas en la que aparece;

print("---------------------------------------------------------")
while pila_aux.size() > 0:
    mcu.push(pila_aux.pop())    # restauro la pila


print("Los personajes que aparecieron en más de 5 películas del MCU son: ")
while mcu.size()>0:
    personaje=mcu.pop()
    if (personaje['apariciones']>5):
        print("- ", personaje['nombre'], 'apareció en ', personaje['apariciones'], " películas")
    pila_aux.push(personaje)


### c. determinar en cuantas películas participo la Viuda Negra (Black Widow);          # ya estaba en el anterior
print("---------------------------------------------------------")
while pila_aux.size() > 0:
    mcu.push(pila_aux.pop())    # restauro la pila

while mcu.size()>0:
    personaje=mcu.pop()
    if (personaje['nombre']== 'Black Widow'):
        print(personaje['nombre'], "participó en ", personaje['apariciones'], " películas")
    pila_aux.push(personaje)


### d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
print("---------------------------------------------------------")
while pila_aux.size() > 0:
    mcu.push(pila_aux.pop())    # restauro la pila

print("Los personajes que empiezan con las letras C, D y G son:")
while mcu.size() > 0:
    personaje=mcu.pop()
    if personaje['nombre'].startswith(('C','D','G')):
        print(personaje['nombre'])
    pila_aux.push(personaje)

print("---------------------------------------------------------")
