"""
2. Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos necesarios para resolver las siguientes tareas: 
    a) cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de episodios en los que aparecieron juntos ambos personajes que se relacionan; 
    b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
    c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son. 
    d) cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, BB-8.
"""
from grafo import Graph

grafo= Graph(dirigido=False)

vertices = [
    "Luke Skywalker", "Han Solo", "Chewbacca", "Princess Leia", "Obi-Wan Kenobi", "Yoda", "Anakin Skywalker", "Darth Vader","Emperor Palpatine", "Padmé Amidala", "Rey", "Finn", "Poe Dameron", "Boba Fett", "C-3PO", "Kylo Ren", "R2-D2", "BB-8"
]

#aristas
datos = [
    {"Personaje A": "Luke Skywalker", "Personaje B": "Han Solo", "Episodios Juntos": 3},
    {"Personaje A": "Han Solo", "Personaje B": "Chewbacca", "Episodios Juntos": 8},
    {"Personaje A": "Princess Leia", "Personaje B": "Han Solo", "Episodios Juntos": 3},
    {"Personaje A": "Obi-Wan Kenobi", "Personaje B": "Yoda", "Episodios Juntos": 2},
    {"Personaje A": "Anakin Skywalker", "Personaje B": "Obi-Wan Kenobi", "Episodios Juntos": 3},
    {"Personaje A": "Darth Vader", "Personaje B": "Emperor Palpatine", "Episodios Juntos": 2},
    {"Personaje A": "Padmé Amidala", "Personaje B": "Anakin Skywalker", "Episodios Juntos": 6},
    {"Personaje A": "Rey", "Personaje B": "Finn", "Episodios Juntos": 2},
    {"Personaje A": "Poe Dameron", "Personaje B": "BB-8", "Episodios Juntos": 2},
    {"Personaje A": "Luke Skywalker", "Personaje B": "Darth Vader", "Episodios Juntos": 3},
    {"Personaje A": "Yoda", "Personaje B": "Obi-Wan Kenobi", "Episodios Juntos": 2},
    {"Personaje A": "Boba Fett", "Personaje B": "Darth Vader", "Episodios Juntos": 4},
    {"Personaje A": "C-3PO", "Personaje B": "Princess Leia", "Episodios Juntos": 1},
    {"Personaje A": "Rey", "Personaje B": "Kylo Ren", "Episodios Juntos": 2},
    {"Personaje A": "Chewbacca", "Personaje B": "Han Solo", "Episodios Juntos": 8},
    {"Personaje A": "R2-D2", "Personaje B": "C-3PO", "Episodios Juntos": 2},
    {"Personaje A": "BB-8", "Personaje B": "Poe Dameron", "Episodios Juntos": 2}
]

for vertice in vertices:
    grafo.insert_vertice(vertice)

for arista in datos: 
    grafo.insert_arista(arista.get("Personaje A"), arista.get("Personaje B"), arista.get("Episodios Juntos"))

print("")
print("------------------------------------")
# b) hallar el árbol de expansión minino y determinar si contiene a Yoda; 
x = grafo.kruskal("BB-8")
print("Árbol de expansión mínima de la casa: ", x)

print("")
contiene_yoda = any("Yoda" in arbol for arbol in x)

if contiene_yoda:
    print("El árbol contiene a Yoda")
else:
    print("El árbol no contiene a Yoda")

print("------------------------------------")
# c) determinar cuál es el número máximo de episodio que comparten dos personajes, y quienes son.
def max_episodios(self):
    max_episodios = 0
    personajes=[]
    for nodo in self.elements:
        for arista in nodo['aristas']:
            if arista['peso'] > max_episodios:
                max_episodios = arista['peso']
                personajes = [[nodo['value'], arista['value']]]
            elif arista['peso'] == max_episodios:
                personajes.append((nodo['value'], arista['value']))

    return max_episodios, personajes

max_episodios, personajes = max_episodios(grafo)
print("El número máximo de episodios compartidos por dos personajes es de: ", max_episodios)
print("Los personajes que comparten estos episodios son: ", personajes)
print("------------------------------------")
