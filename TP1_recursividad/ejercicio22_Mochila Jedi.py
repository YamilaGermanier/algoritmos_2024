"""22. El problema de la mochila Jedi. Suponga que un Jedi (Luke Skywalker, Obi-Wan Kenobi, Rey u otro, el que más le guste) 
está atrapado, pero muy cerca está su mochila que contiene muchos objetos. Implementar una función recursiva llamada 
“usar la fuerza” que le permita al Jedi “con ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no queden más objetos en la mochila;
b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sacar para encontrarlo;
c. Utilizar un vector para representar la mochila."""

mochila = ['túnica', 'comunicador', 'datapad', 'créditos galácticos','sable de luz', 'mapa estelar']
cont=0

def usarLaFuerza(vector):
    if len(vector) == 0:
        return 0
    else:
        if vector[0] == 'sable de luz':
            return 1
        else:
            global cont   # definir la variable como global para poder utilizarla
            cont+=1
            return usarLaFuerza(vector[1:])
    
if usarLaFuerza(mochila) == 1:
    print("El sable de luz se encuentra en la mochila. Ahsoka Tano necesitó sacar", cont, "objetos para encontrarlo.")
else:
    print("El sable de luz no se encuentra en la mochila de Ahsoka Tano.")