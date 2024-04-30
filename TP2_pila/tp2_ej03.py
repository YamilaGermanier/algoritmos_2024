# Reemplazar todas las ocurrencias de un determinado elemento en una pila.
from tp2_pila import Stack
from random import randint

pila=Stack()
pila_aux=Stack()

for i in range(10):
    pila.push(randint(1, 10)) # Cargo elementos

print(pila.on_top())

buscado = int(input("Ingrese el número a buscar: ")) # entro el valor a buscar
reemplazo = int(input("Ingrese el número reemplazante: "))


def reemplazar():
    while pila.size()>0:    # mientras halla elementos
        if pila.on_top() == buscado:    # veo si es igual
            pila.pop()      # acá los elimino
            pila.push(reemplazo)
            pila_aux.push(pila.pop())     # acá sí los mando a la auxiliar
        else:
            data= pila.pop()
            pila_aux.push(data)   #mando igual a la auxiliar
    return None

reemplazar()
print("tamaño pila", pila.size())   #compruebo que esté vacía
print("tamaño auxiliar", pila_aux.size())   #compruebo que esté llena
print("top pila auxiliar", pila_aux.on_top())     #veo orden

while pila_aux.size() > 0:
    pila.push(pila_aux.pop())   # volviendo los datos para no perder nada

print("on top pila: ", pila.on_top())   # confirmo el orden