"""6. Dada una lista de superhéroes de comics, de los cuales se conoce su nombre, año aparición,
casa de comic a la que pertenece (Marvel o DC) y biografía, implementar la funciones necesarias
para poder realizar las siguientes actividades:

a. eliminar el nodo que contiene la información de Linterna Verde;
b. mostrar el año de aparición de Wolverine;
c. cambiar la casa de Dr. Strange a Marvel;
d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra
“traje” o “armadura”;
e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963;
f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
g. mostrar toda la información de Flash y Star-Lord;
h. listar los superhéroes que comienzan con la letra B, M y S;
i. determinar cuántos superhéroes hay de cada casa de comic."""

from lista import super_heroes, search, remove
from ejemplo import by_name, by_house

#Encontrar a Linterna Verde
index = search(super_heroes, 'nombre', 'Linterna Verde')
if index is not None:
    print(f"El año de aparición de {super_heroes[index]['nombre']} es {super_heroes[index]['año_aparicion']}")

# a. eliminar el nodo que contiene la información de Linterna Verde;
eliminado = remove(super_heroes,'nombre','Linterna Verde')
print("El siguiente nodo ha sido eliminado:", eliminado)

# b. mostrar el año de aparición de Wolverine;
index = search(super_heroes, 'nombre', 'Wolverine')
if index is not None:
    print(f"El año de aparición de {super_heroes[index]['nombre']} es {super_heroes[index]['año_aparicion']}")

# c. cambiar la casa de Dr. Strange a Marvel;
index = search(super_heroes, 'nombre', 'Doctor Strange')
if super_heroes[index]['casa_comic'] != 'Marvel':
    super_heroes[index]['casa_comic'] = 'Marvel'
print(f"La casa de {super_heroes[index]['nombre']} es {super_heroes[index]['casa_comic']}")

## EJEMPLO if 'traje' in [biografria]
# d. mostrar el nombre de aquellos superhéroes que en su biografía menciona la palabra “traje” o “armadura”
for i in range(len(super_heroes)):
    if ('traje' in super_heroes[i]['biografia'] or 'armadura' in super_heroes[i]['biografia']):
        print(f"Los personajes con trajes o armaduras son: {super_heroes[i]['nombre']}")
"""
EJEMPLO PROFESOR
Función enumerate devuelve índice y valor, queda más legible

for index, heroe in enumerate(super_heroes):
    if 'traje' in heroe['biografia'] or 'armadura' in heroe['biografia']:
        print(index, heroe['nombre'], heroe['biografia'])

también:
for elemento in lista:

"""

print()

#e. mostrar el nombre y la casa de los superhéroes cuya fecha de aparición sea anterior a 1963
super_heroes.sort(key=by_house)
print("Superhéroes anteriores a 1963: ")
for i in range(len(super_heroes)):
    if (super_heroes[i]['año_aparicion'] < 1963):
        print(super_heroes[i]['nombre']," - ", super_heroes[i]['casa_comic'])

# f. mostrar la casa a la que pertenece Capitana Marvel y Mujer Maravilla;
index=search(super_heroes, 'nombre', 'Mujer Maravilla')
if index is not None:
    print(f"El personade de la {super_heroes[index]['nombre']} pertenece a la casa de {super_heroes[index]['casa_comic']} ")
index=search(super_heroes, 'nombre', 'Capitana Marvel')
if index is not None:
    print(f"El personade de la {super_heroes[index]['nombre']} pertenece a la casa de {super_heroes[index]['casa_comic']} ")
print()
# g. mostrar toda la información de Flash y Star-Lord;
for i in range(len(super_heroes)):
    if super_heroes[i]['nombre'] == 'Flash' or super_heroes[i]['nombre'] == 'Star-Lord':
        print(super_heroes[i])
print()

# h. listar los superhéroes que comienzan con la letra B, M y S;
super_heroes.sort(key=by_name)
print("Listado de superhéroes con las letras B, M y S:")
for i in range(len(super_heroes)):
    if super_heroes[i]['nombre'][0]== 'B' or super_heroes[i]['nombre'][0]== 'M' or super_heroes[i]['nombre'][0]== 'S':
        print(super_heroes[i]['nombre'])
        
        
"""
CLASE: recomienda usar startswith ya que si fueran dos o más letras no se puede con sólo poner la ubicación.
por ejemplo:

for elemento in list:
    if list['nombre'].startswith('Ba', 'Sp'): (acepta varios criterios)
        print(list['nombre'])
"""

print()

# i. determinar cuántos superhéroes hay de cada casa de comic
marvel=0
dc = 0
otros=0
for i in range(len(super_heroes)):
    if super_heroes[i]['casa_comic']== "Marvel Comics":
        marvel+=1
    elif super_heroes[i]['casa_comic'] == "DC Comics":
        dc+=1
    else:
        otros+=1
print("Cantidad de superheroes en Marvel Comics:", marvel)
print("Cantidad de superheroes en DC Comics:", dc)
print("Cantidad de superheroes en otras casas de comics:", otros)