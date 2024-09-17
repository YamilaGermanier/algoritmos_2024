"""
11. Dada una cola con personajes de la saga Star Wars, de los cuales se conoce su nombre y planeta
de origen. Desarrollar las funciones necesarias para resolver las siguientes actividades:
    a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
    b. indicar el plantea natal de Luke Skywalker y Han Solo
    c. insertar un nuevo personaje antes del maestro Yoda
    d. eliminar el personaje ubicado después de Jar Jar Binks
"""
from cola import Queue

personajes = [
        ('Padme Amidala', 'Naboo'), ('Leia Organa', 'Alderaan'),('Luke Skywalker', 'Tatooine'),('Han Solo', 'Cordellia'),
        ('Darth Vader', 'Tatooine'),('Ewoks', 'Endor'), ('Jar Jar Binks', 'Naboo'),('Cara Dune', 'Alderaan'), ('Yoda', 'Desconocido')
        ]


class Personaje (object):

    def __init__(self, nombre, planeta):
        self.nombre = nombre
        self.planeta = planeta

    def __str__(self):
        return self.nombre + ' - ' + self.planeta

cola_personajes = Queue()
cola_aux= Queue()

for (a,b) in personajes:
    personaje= Personaje(a,b)
    cola_personajes.arrive(personaje)


#  a. mostrar los personajes del planeta Alderaan, Endor y Tatooine
def mostrar_perso(cola, planeta_buscado):
    print ('Lista de personajes de', planeta_buscado)
    cola_aux= Queue()
    while (cola_personajes.size() > 0):
        x = cola_personajes.attention()
        cola_aux.arrive(x)
        if (x.planeta == planeta_buscado):
            print (x.nombre)
    while (cola_aux.size() > 0):
        cola_personajes.arrive(cola_aux.attention())

mostrar_perso(cola_personajes, 'Tatooine')
print()
mostrar_perso(cola_personajes, 'Alderaan')
print()
mostrar_perso(cola_personajes, 'Endor')

print("----------------------------------")

# b. indicar el plantea natal de Luke Skywalker y Han Solo
def planeta_natal(cola, perso_buscado):
    print("El planeta natal de ", perso_buscado, "es: ")
    while (cola_personajes.size() > 0):
        x = cola_personajes.attention()
        cola_aux.arrive(x)
        if (x.nombre == perso_buscado):
            print (x.planeta)
    while (cola_aux.size() > 0):
        cola_personajes.arrive(cola_aux.attention())

planeta_natal(cola_personajes, 'Luke Skywalker')
print()
planeta_natal(cola_personajes, 'Han Solo')
print()

print("----------------------------------")

# c. insertar un nuevo personaje antes del maestro Yoda
def insertar_antes (cola, perso1, perso2):
    cola_aux = Queue()
    while (cola_personajes.size() > 0):
        x = cola_personajes.attention()
        if (x.nombre==perso1):
            cola_aux.arrive(perso2)
        cola_aux.arrive(x)
    
    while (cola_personajes.size() > 0):
        cola_aux.arrive(cola_personajes.attention())
    while (cola_aux.size() > 0):
        cola_personajes.arrive(cola_aux.attention())

perso2=Personaje("Grogu", "Desconocido")
insertar_antes(cola_personajes, 'Yoda', perso2)

#while (cola_personajes.size() > 0):
 #   print(cola_personajes.attention())

print("----------------------------------")

# d. eliminar el personaje ubicado después de Jar Jar Binks
def eliminar_despues (cola, perso1):
    cola_aux = Queue()
    while (cola_personajes.size() > 0):
        x = cola_personajes.attention()
        cola_aux.arrive(x)
        if (x.nombre==perso1):
            break
    cola_personajes.attention()
    while (cola_personajes.size() > 0):
        cola_aux.arrive(cola_personajes.attention())
    while (cola_aux.size() > 0):
        cola_personajes.arrive(cola_aux.attention())

eliminar_despues(cola_personajes, 'Jar Jar Binks')

#while (cola_personajes.size() > 0):
 #   print(cola_personajes.attention())

print("----------------------------------")