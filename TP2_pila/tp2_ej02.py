# Eliminar de una pila todos los elementos impares, es decir que en la misma solo queden números pares.

from tp2_pila import Stack
from random import randint

pila = Stack()
pila_aux = Stack()

for i in range(10):
    pila.push(randint(1, 99)) # Cargo elementos


while pila.size() > 0:  #mientras halla elementos
    data = pila.pop() #voy sacando elemento a elemento
    if data % 2 == 0:   # si es par entonces:
        pila_aux.push(data) # se guarda en lista auxiliar
    
while pila_aux.size() > 0: # mientras halla elementos en lista auxiliar
    pila.push(pila_aux.pop())   # cargo los elementos desde la auxiliar a la original


print()
print(pila.size()) # muestra el tamaño de la pila (los números pares que quedaron)