"""
15. Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
    a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
    uno en las naturales) y tipo (natural o arquitectónica);
    b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
    la distancia que las separa;
    c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
    d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
    e. determinar si algún país tiene más de una maravilla del mismo tipo;
    f. deberá utilizar un grafo no dirigido.
"""

from grafo import Graph
from random import randint


# f. deberá utilizar un grafo no dirigido.
grafo = Graph(dirigido=False)

# a. de cada una de las maravillas se conoce:
# su nombre, país de ubicación y tipo (natural o arquitectónica);
arquitectonicas=[
    {'nombre': 'Chichén Itzá', 'datos': {'pais': ['México'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Cristo Redentor', 'datos': {'pais': ['Brasil'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Machu Picchu', 'datos': {'pais': ['Perú'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Gran Muralla China', 'datos': {'pais': ['China'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Petra', 'datos': {'pais': ['Jordania'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Coliseo', 'datos': {'pais':[ 'Italia'], 'tipo': 'arquitectónica'}},
    {'nombre': 'Taj Mahal', 'datos': {'pais': ['India'], 'tipo': 'arquitectónica'}}
]

naturales=[
    {'nombre': 'Amazonas', 'datos': {'pais': ['Brasil'], 'tipo': 'natural'}},
    {'nombre': 'Bahía de Ha-Long', 'datos': {'pais': ['Vietnam'], 'tipo': 'natural'}},
    {'nombre': 'Cataratas del Iguazú', 'datos': {'pais': ['Argentina', 'Brasil'], 'tipo': 'natural'}},
    {'nombre': 'Isla Jeju', 'datos': {'pais': ['Corea del Sur'], 'tipo': 'natural'}},
    {'nombre': 'Parque Nacional de Komodo', 'datos': {'pais': ['Indonesia'], 'tipo': 'natural'}},
    {'nombre': 'Río Subterráneo de Puerto Princesa', 'datos': {'pais': ['Filipinas'], 'tipo': 'natural'}},
    {'nombre': 'Montaña de la Mesa', 'datos': {'pais': ['Sudáfrica'], 'tipo': 'natural'}}
]

for e in range (2):
    maravillas = arquitectonicas if e == 0 else naturales
    for maravilla in maravillas:
        grafo.insert_vertice(maravilla['nombre'], maravilla['datos'])

# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
for e in range (2):
    maravillas = arquitectonicas if e == 0 else naturales
    for i in range(0, len(maravillas)-1):
        for j in range(i+1, len(maravillas)):
            grafo.insert_arista(maravillas[i]['nombre'], maravillas[j]['nombre'], randint(1500, 15000))

print("")
print("-----------")

# c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
arbol_min_arq = grafo.kruskal(arquitectonicas[0]['nombre'])
print("Árbol de expansión mínimo para las maravillas arquitectónicas:")
print(arbol_min_arq)
print("")

arbol_min_nat = grafo.kruskal(naturales[0]['nombre'])
print("Árbol de expansión mínimo para las maravillas naturales:")
print(arbol_min_nat)
print("")
print("-----------")

# d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
paises_arq = set()
for maravilla in arquitectonicas:
    for pais in maravilla['datos']['pais']:
        paises_arq.add(pais)

paises_nat = set()
for maravilla in naturales:
    for pais in maravilla['datos']['pais']:
        paises_nat.add(pais)

paises_mixtos = paises_arq.intersection(paises_nat)
if paises_mixtos:
    for pais in paises_mixtos:
        print(f"En {pais} existen maravillas arquitectónicas y naturales.")
else:
    print("No existen países con maravillas de ambos tipos.")

print("-----------")

# e. determinar si algún país tiene más de una maravilla del mismo tipo;
def maravillas_por_tipo(maravillas, tipo):
    cont_paises = {}
    for maravilla in maravillas:
        for pais in maravilla['datos']['pais']:
            if pais in cont_paises:
                cont_paises[pais] += 1 
            else:
                cont_paises[pais] = 1 

    for pais, cuenta in cont_paises.items():
        if cuenta > 1:
            print(f"En {pais} hay más de una maravilla {tipo}")

# Verificación para arquitectónicas y naturales
maravillas_por_tipo(arquitectonicas, "arquitectónica")
maravillas_por_tipo(naturales, "natural")
print("-----------")