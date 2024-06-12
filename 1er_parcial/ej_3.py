"""
3. Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, maestros, 
colores de sable de luz usados y especie. implementar las funciones
necesarias para resolver las actividades enumeradas a continuación:
    a) listado ordenado por nombre y por especie;
    b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
    c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
    d) mostrar los Jedi de especie humana y twi'lek;
    e) listar todos los Jedi que comienzan con A;
    f) mostrar los Jedi que usaron sable de luz de más de un color;
    g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
    h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
    i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
"""

from Jedi import jedis

####### a) listado ordenado por nombre y por especie;

def by_name(jedi):
    return jedi['name']

def by_species(jedi):
    if jedi['species'] is None:
        return 'None'
    else:
        return jedi['species']

jedis.sort(key=by_name)
# control
for jedi in jedis:
    print(jedi['name'])

print("----------------------------------------------------")

jedis.sort(key=by_species)
for jedi in jedis:
    print(jedi['species'], jedi['name'])

print("----------------------------------------------------")



##### b) mostrar toda la información de Ahsoka Tano y Kit Fisto;
def buscar(jedis):
    for jedi in jedis:
        if jedi['name']== 'Ahsoka Tano' or jedi['name']== 'Kit Fisto':
            print(jedi)

buscar(jedis)

print("----------------------------------------------------")

##### c) mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
def padawans(jedis):
    for jedi in jedis:
        if jedi['master']== 'Yoda' or jedi['master']== 'Luke Skywalker':
            print(jedi['name'], "es el padawan de ", jedi['master'])

padawans(jedis)

print("----------------------------------------------------")

##### d) mostrar los Jedi de especie humana y twi'lek;

def humans_twilek():
    for jedi in jedis:
        if jedi['species']== 'Human' or jedi['species']== "Twi'lek":
            print(jedi['name'], "es de la especie ", jedi['species'])

humans_twilek()

print("----------------------------------------------------")

##### e) listar todos los Jedi que comienzan con A;
lista= []
def listar_a():
    for jedi in jedis:
        if jedi['name'].startswith('A'):
            lista.append(jedi['name'])

listar_a()

print("Jedi que empiezan con la letra A")
for element in lista:
    print(element)

print("----------------------------------------------------")

##### f) mostrar los Jedi que usaron sable de luz de más de un color;
lista_sables = []
def muchos_sables():
    for jedi in jedis:
        if jedi['lightsaber_color'] is not None and '/' in jedi['lightsaber_color']:
            lista_sables.append(jedi['name'])

muchos_sables()

print("Los jedis que usaron muchos sables son:")
for jedi in lista_sables:
    print(jedi)

print("----------------------------------------------------")

#####  g) indicar los Jedi que utilizaron sable de luz amarillo o violeta;
def sables():
    for jedi in jedis:
        if jedi['lightsaber_color'] is not None and ('Yellow' in jedi['lightsaber_color'] or 'Violet' in jedi['lightsaber_color']):
            print(jedi['name'])

sables()


print("----------------------------------------------------")

#####  h) indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.
def pada(jedis):
    for jedi in jedis:
        if jedi['master']== 'Qui-Gon Jin' or jedi['master']== ' Mace Windu':
            print(jedi['name'], "es el padawan de ", jedi['master'])

pada(jedis)

print("----------------------------------------------------")

##### i) Mostrar todos los Jedi que tengan el ranking de Grand Master.
def grandMaster():
    for jedi in jedis:
        if jedi['rank']== 'Grand Master':
            print(jedi['name'])

print("Los jedis con títulos de Grand Master son:")
grandMaster()
