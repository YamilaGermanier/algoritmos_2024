"""
Primer Parcial Algoritmos y Estructuras de Datos

1. Desarrollar una función recursiva que permita listar los elementos de vector/lista de
manera inversa al que están cargados. Preferentemente la función solo debe tener un
parámetro que es la lista de elementos. 

"""

def inversa(lista):
    if len(lista) ==0:
        return "La lista está vacía"
    else:
        return [lista[-1]] + inversa(lista[:-1])
    
# control
#alumnos= ['Juan', 'Maria', 'Bautista', 'Jeremías', 'Antoine']
lista=[]
print(inversa(lista))