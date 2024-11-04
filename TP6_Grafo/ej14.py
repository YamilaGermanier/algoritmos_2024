"""
Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
    a. cada vértice representar un nodo de una casa: cocina, comedor, cochera, quincho,
    baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
    b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el distancia de la arista es la distancia entre los nodos, se debe cargar en metros;
    c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
    para conectar todos los nodos;
    d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
    determinar cuántos metros de cable de red se necesitan para conectar el router con el
    Smart Tv
"""

from grafo import Graph

print("")

# Implementar sobre un grafo no dirigido
grafo = Graph(dirigido=False)

# nodos de la casa
nodos = ["cocina", "comedor", "cochera", "quincho", "baño 1", "baño 2",
             "habitación 1", "habitación 2", "sala de estar", "terraza", "patio"]

for nodo in nodos:
    grafo.insert_vertice(nodo)

# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el distancia de la arista # es la distancia entre los nodos, se debe cargar en metros;

grafo.insert_arista("cocina", "comedor", 1)
grafo.insert_arista("cocina", "baño 1", 5)
grafo.insert_arista("cocina", "habitación 1", 8)
##3
grafo.insert_arista("comedor", "sala de estar", 4)
grafo.insert_arista("comedor", "baño 1", 5)
grafo.insert_arista("comedor", "quincho", 10)
grafo.insert_arista("comedor", "baño 2", 9)
grafo.insert_arista("comedor", "cocina", 1)
## 5
grafo.insert_arista("cochera", "patio", 10)
grafo.insert_arista("cochera", "quincho", 12)
grafo.insert_arista("cochera", "habitación 2", 8)
grafo.insert_arista("cochera", "baño 1", 7)
grafo.insert_arista("cochera", "sala de estar", 7)
# 5
grafo.insert_arista("quincho", "terraza", 15)
grafo.insert_arista("quincho", "baño 1", 4)
grafo.insert_arista("quincho", "baño 2", 8)
# 3
grafo.insert_arista("baño 1", "baño 2", 9)
grafo.insert_arista("baño 1", "comedor", 5)
grafo.insert_arista("baño 1", "cocina", 5)

grafo.insert_arista("baño 2", "habitación 2", 2)
grafo.insert_arista("baño 2", "quincho", 8)
grafo.insert_arista("baño 2", "comedor", 9)

grafo.insert_arista("habitación 1", "habitación 2", 8)
grafo.insert_arista("habitación 1", "cocina", 8)
grafo.insert_arista("habitación 1", "quincho", 12)

grafo.insert_arista("habitación 2", "habitación 1", 8)
grafo.insert_arista("habitación 2", "sala de estar", 9)
grafo.insert_arista("habitación 2", "cochera", 8)

grafo.insert_arista("terraza", "patio", 10)
grafo.insert_arista("terraza", "sala de estar", 8)
grafo.insert_arista("terraza", "quinchi", 15)

grafo.insert_arista("sala de estar", "terraza", 8)
grafo.insert_arista("sala de estar", "habitación 2", 9)
grafo.insert_arista("sala de estar", "comedor", 4)

grafo.insert_arista("quincho", "habitación 1", 12)
grafo.insert_arista("quincho", "baño 2", 8)
grafo.insert_arista("quincho", "comedor", 10)

grafo.insert_arista("patio", "terraza", 10)
grafo.insert_arista("patio", "cochera", 10)
grafo.insert_arista("patio", "baño 2", 2)

print("---------------------------")
# c. obtener el árbol de expansión mínima;
x = grafo.kruskal("sala de estar")
print("Árbol de expansión mínima de la casa: ", x)

# Calcular la longitud total de cables del árbol de expansión mínima
t_cable=0

#### origen - destino - metros ; otro
for elemento in grafo.kruskal("sala de estar")[0].split(';'): #separo cada elemento
    t_cable += int(elemento.split('-')[-1]) # separo y me quedo con los metros
print(f"Se necesitan {t_cable} metros de cable para conectar todos los nodos")

print("---------------------------")

# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
# determinar cuántos metros de cable de red se necesitan para conectar el router con el
# Smart Tv
camino=grafo.dijkstra("habitación 1")
destino="sala de estar"
camino_corto=[]
distancia=0
encontrado= False
while camino.size()>0 :
    nodo= camino.pop()
    if nodo[1][0] == destino:
        #print(nodo[1][0])
        camino_corto.append(nodo[1][0])
        destino=nodo[1][2]
        while encontrado == False:
            distancia+=nodo[0]
            encontrado = True


camino_corto.reverse()        
print(f"El camino mas corto desde la habitacion 1 hasta la sala de estar es {camino_corto}, y la distancia total es de {distancia} metros")
print("---------------------------")