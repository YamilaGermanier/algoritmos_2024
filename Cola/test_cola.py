from cola import Queue
from ..TP2_pila.tp2_pila import Stack # importación relativa from ..NombreCarpeta.nombreArchivo import NombreFunción
from random import randint


cola_char = Queue()

for i in range(10):
    letra = chr(randint(65, 90))
    cola_char.arrive(letra)

for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()

print()
vocales = ['A', 'E', 'I', 'O', 'U']

for i in range(cola_char.size()):
    if cola_char.on_front() in vocales:
        cola_char.attention()
    else:
        cola_char.move_to_end()

for i in range(cola_char.size()):
    print(cola_char.on_front())
    cola_char.move_to_end()