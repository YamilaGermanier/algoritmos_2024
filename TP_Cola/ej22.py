"""
22. Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), de los cuales se conoce
el nombre del personaje, el nombre del superhéroe y su género (Masculino M y Femenino
F), por ejemplo {Tony Stark, Iron Man, M}, {Steve Rogers, Capitán América, M}, {Natasha Romanoff,
Black Widow, F}, etc., desarrollar un algoritmo que resuelva las siguientes actividades:
    a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
    b. mostrar los nombre de los superhéroes femeninos;
    c. mostrar los nombres de los personajes masculinos;
    d. determinar el nombre del superhéroe del personaje Scott Lang;
    e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
    con la letra S;
    f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
    de superhéroes.
"""

from cola import Queue

personajes = [
    ("Tony Stark", "Iron Man", "M"), ("Steve Rogers", "Capitán América", "M"), ("Natasha Romanoff", "Black Widow", "F"), 
    ("Carol Danvers", "Capitana Marvel", "F"), ("Peter Parker", "Spider-Man", "M"), ("Wanda Maximoff", "Scarlett Withc", "F"),
    ("Scott Lang","Ant-Man","M")
]

class Personaje (object):

    def __init__(self, nombre, s_heroe, genero):
        self.nombre = nombre
        self.s_heroe = s_heroe
        self.genero = genero

    def __str__(self):
        return self.nombre + ' - ' + self.s_heroe + ' - ' + self.genero

cola_personajes = Queue()
cola_F = Queue()
cola_M = Queue()
cola_con_S = Queue()
cola_aux= Queue()

for (a,b,c) in personajes:
    perso= Personaje(a,b,c)
    cola_personajes.arrive(perso)


while (cola_personajes.size()>0):
    x = cola_personajes.attention()
    if (x.s_heroe == "Capitana Marvel"):
        print ('El nombre de', x.s_heroe, 'es', x.nombre)
    if (x.genero == "F"):
        cola_F.arrive(x)
    if (x.genero == "M"):
        cola_M.arrive(x)
    if (x.nombre == "Scott Lang"):
        print ('El nombre de super heroe de Scott Lang es', x.s_heroe)
    if (x.nombre.startswith("S") or x.s_heroe.startswith("S")):
        cola_con_S.arrive(x)
    if (x.nombre == "Carol Danvers"):
        print ('El nombre de super heroe de Carol Danvers es', x.s_heroe)
print()
print("--------------------")

print("Nombres de los superhéroes femeninos:")
while (cola_F.size() > 0):
    print(cola_F.attention().nombre)
print()
print("--------------------")
print("Nombres de los superhéroes masculinos:")
while (cola_M.size() > 0):
    print(cola_M.attention().nombre)
print()
print("--------------------")

print("Superhéroes o Personajes cuyos nombres comienzan con la letra S")
while (cola_con_S.size() > 0):
    print(cola_con_S.attention())