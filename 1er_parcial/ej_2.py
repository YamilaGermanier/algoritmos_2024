"""
2. Dada una pila con los datos de dinosaurios resolver lo siguiente actividades:
    a) Contar cuantas especies hay;
    b) Determinar cuantos descubridores distintos hay;
    c) Mostrar todos los dinosaurios que empiecen con T;
    d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
    e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
"""

from pila import Pila
from dino import dinosaurios

pila_dino= Pila()

for dino in dinosaurios:
    pila_dino.push(dino)

print(pila_dino.on_top()) # control de carga

print("----------------------------------------------")

# a) Contar cuantas especies hay;
pila_aux= Pila()
list_especies= []
while pila_dino.size()>0:
    dino= pila_dino.pop()
    if dino['especie'] not in list_especies:
        list_especies.append(dino['especie'])
    pila_aux.push(dino)

print("La cantidad de especies de dinosaurios es: ", len(list_especies))

while pila_aux.size()>0:
        pila_dino.push(pila_aux.pop())

print("----------------------------------------------")

# b) Determinar cuantos descubridores distintos hay;

list_descubridores= []
while pila_dino.size()>0:
    dino= pila_dino.pop()
    if dino['descubridor'] not in list_descubridores:
        list_descubridores.append(dino['descubridor'])
    pila_aux.push(dino)

print("La cantidad de descubridores de dinosaurios que hay es: ", len(list_descubridores))

while pila_aux.size()>0:
        pila_dino.push(pila_aux.pop())

print("----------------------------------------------")

# c) Mostrar todos los dinosaurios que empiecen con T;
print("Lista de dinosaurios que empiezan con la letra T")
while pila_dino.size()>0:
    dino = pila_dino.pop()
    if dino['nombre'].startswith('T'):
          print(dino['nombre'])
    pila_aux.push(dino)

while pila_aux.size()>0:
        pila_dino.push(pila_aux.pop())

print("----------------------------------------------")

# d) Mostrar todos los dinosaurio que pesen menos de 275 Kg
print("Dinosaurios que pesen menos de 275 Kg:")
while pila_dino.size()>0:
    dino=pila_dino.pop()
    if int(dino['peso'].split()[0]) < 275:
        print(dino['nombre'])
    pila_aux.push(dino)

while pila_aux.size()>0:
        pila_dino.push(pila_aux.pop())

print("----------------------------------------------")

# e) Dejar en una pila aparte todos los dinosaurios que comienzan con A, Q, S;
pila_e = Pila()
while pila_dino.size() > 0:
    dino = pila_dino.pop()
    if dino['nombre'].startswith(('A', 'Q', 'S')):
        pila_e.push(dino)
    pila_aux.push(dino)

print("tamaño de la lista aparte: ", pila_e.size())
print("Dinosaurios que comienzan con A, Q, S:")
while pila_e.size() > 0:
    dino= pila_e.pop()
    print(dino['nombre'])

while pila_aux.size()>0:
        pila_dino.push(pila_aux.pop())

print("----------------------------------------------")