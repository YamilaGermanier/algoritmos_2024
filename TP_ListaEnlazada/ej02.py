#Diseñar un algoritmo que elimine todas las vocales que se encuentren en una lista de caracteres.

lista = ['a', 'o', 'a', 'b', 'd', 'e', 't', 'i', 'o', 'a', 'x', 'u', 'y', 'u', 'z', 'a']
vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

print(len(lista))
print()
print(lista)

for elemento in lista:
    if elemento in vocales:
        # lista.remove(elemento) me elimina el primero o los primeros, y si están desordenadas no elimina hasta que llega
        lista.remove(elemento)
print()
print(len(lista))
print(lista)