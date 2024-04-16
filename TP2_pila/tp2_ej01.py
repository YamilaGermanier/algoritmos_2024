# Determinar el número de ocurrencias de un determinado elemento en una pila.

from tp2_pila import Stack
from random import randint

pila= Stack() # inicializo
pila_aux = Stack() # inicializo la auxiliar

for i in range(10):
    pila.push(randint(1, 5)) # cargo valores random no tan altos para probar

print(pila.on_top()) # veo cuál está arriba para saber

buscado = int(input("Ingrese el número a buscar: ")) # entro el valor a buscar

def buscar(buscado, pila_aux):
    cont=0
    while pila.size()>0:    # mientras halla elementos
        if pila.on_top() == buscado:    # veo si es igual
            data= pila.pop()      # acá los elimino (no dice nada de guardarlos...)
            cont+=1
            pila_aux.push(data)     # acá sí los mando a la auxiliar
        else:
            data= pila.pop()
            pila_aux.push(data)
    return cont     # me devuelve el número de veces que aparece



while pila_aux.size() > 0:
    pila.push(pila_aux.pop())   # volviendo los datos para no perder nada

print(pila.on_top())

x=buscar(buscado, pila_aux)
    
print("El número buscado aparece: ", x, "veces")
