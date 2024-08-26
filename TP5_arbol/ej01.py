"""
1. Desarrollar un algoritmo que permita cargar 1000 número enteros –generados de manera aleatoria–
que resuelva las siguientes actividades:
    a. realizar los barridos preorden, inorden, postorden y por nivel sobre el árbol generado;
    b. determinar si un número está cargado en el árbol o no;
    c. eliminar tres valores del árbol;
    d. determinar la altura del subárbol izquierdo y del subárbol derecho;
    e. determinar la cantidad de ocurrencias de un elemento en el árbol;
    f. contar cuántos números pares e impares hay en el árbol.
"""

from arbol import BinaryTree
from random import randint

tree = BinaryTree()

for i in range(10):
    tree = tree.insert_node(randint(1,15))

pos = tree.search(10)
if pos:
    print('lo encontre', pos.value)
else:
    print('no esta')