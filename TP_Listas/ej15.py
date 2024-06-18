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
from TP_Listas.lista_ejemplo import show_list_list, by_name, search

entrenadores = [
    {
        "nombre": "Ash Ketchum",
        "torneos_ganados": 7,
        "batallas_perdidas": 50,
        "batallas_ganadas": 120
    },
    {
        "nombre": "Goh",
        "torneos_ganados": 2,
        "batallas_perdidas": 10,
        "batallas_ganadas": 40
    },
    {
        "nombre": "Leon",
        "torneos_ganados": 10,
        "batallas_perdidas": 5,
        "batallas_ganadas": 100
    },
    {
        "nombre": "Chloe",
        "torneos_ganados": 1,
        "batallas_perdidas": 8,
        "batallas_ganadas": 30
    },
    {
        "nombre": "Raihan",
        "torneos_ganados": 4,
        "batallas_perdidas": 15,
        "batallas_ganadas": 60
    }
]

pokemons = [
    {
        "nombre": "Pikachu",
        "nivel": 35,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Pikachu",
        "nivel": 20,
        "tipo": "Eléctrico",
        "subtipo": None
    },
    {
        "nombre": "Charizard",
        "nivel": 40,
        "tipo": "Fuego",
        "subtipo": "Volador"
    },
    {
        "nombre": "Bulbasaur",
        "nivel": 30,
        "tipo": "Planta",
        "subtipo": "Veneno"
    },
    {
        "nombre": "Starmie",
        "nivel": 30,
        "tipo": "Agua",
        "subtipo": "Psíquico"
    },
    {
        "nombre": "Psyduck",
        "nivel": 25,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Gyarados",
        "nivel": 35,
        "tipo": "Agua",
        "subtipo": "Volador"
    },
    {
        "nombre": "Onix",
        "nivel": 38,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Geodude",
        "nivel": 28,
        "tipo": "Roca",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Vulpix",
        "nivel": 20,
        "tipo": "Fuego",
        "subtipo": None
    },
    {
        "nombre": "Blastoise",
        "nivel": 50,
        "tipo": "Agua",
        "subtipo": None
    },
    {
        "nombre": "Umbreon",
        "nivel": 45,
        "tipo": "Siniestro",
        "subtipo": None
    },
    {
        "nombre": "Nidoking",
        "nivel": 40,
        "tipo": "Veneno",
        "subtipo": "Tierra"
    },
    {
        "nombre": "Dragonite",
        "nivel": 55,
        "tipo": "Dragón",
        "subtipo": "Volador"
    },
    {
        "nombre": "Aerodactyl",
        "nivel": 52,
        "tipo": "Roca",
        "subtipo": "Volador"
    }
]

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