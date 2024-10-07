"""
Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
resuelva las siguientes consultas:
    a. listado inorden de las criaturas y quienes la derrotaron;
    b. se debe permitir cargar una breve descripción sobre cada criatura;
    c. mostrar toda la información de la criatura Talos;
    d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
    e. listar las criaturas derrotadas por Heracles;
    f. listar las criaturas que no han sido derrotadas;
    g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
    o dios que la capturo;
    h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
    Erimanto indicando que Heracles las atrapó;
    i. se debe permitir búsquedas por coincidencia;
    j. eliminar al Basilisco y a las Sirenas;
    k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
    derroto a varias;
    l. modifique el nombre de la criatura Ladón por Dragón Ladón;
    m. realizar un listado por nivel del árbol;
    n. muestre las criaturas capturadas por Heracles.
"""
# DATOS:
# Nombre de Criatura --- Derrotada por --- Descripción --- Capturada por ---

from arbol_avl import BinaryTree

arbol = BinaryTree()

criaturas = [
{"nombre": "Ceto", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Tifon", "derrotado_por": "Zeus","descripcion":"","capturada_por": ""},
{"nombre": "Equidna", "derrotado_por": "Argos Panoptes","capturada_por": ""},
{"nombre": "Dino", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Pefredo", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Enio", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Escila", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Caribdis", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Euriale", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Esteno", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Medusa", "derrotado_por": "Perseo","descripcion":"","capturada_por": ""},
{"nombre": "Ladon", "derrotado_por": "Heracles","descripcion":"","capturada_por": ""},
{"nombre": "Aguila del Caucaso", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Quimera", "derrotado_por": "Belerofonte","descripcion":"","capturada_por": ""},
{"nombre": "Hidra de Lerna", "derrotado_por": "Heracles","descripcion":"","capturada_por": ""},
{"nombre": "Leon de Nemea", "derrotado_por": "Heracles","descripcion":"","capturada_por": ""},
{"nombre": "Esfinge", "derrotado_por": "Edipo","descripcion":"","capturada_por": ""},
{"nombre": "Dragon de la Colquida", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Cerbero", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Cerda de Cromion", "derrotado_por": "Teseo","descripcion":"","capturada_por": ""},
{"nombre": "Ortro", "derrotado_por": "Heracles","descripcion":"","capturada_por": ""},
{"nombre": "Toro de Creta", "derrotado_por": "Teseo","descripcion":"","capturada_por": ""},
{"nombre": "Jabali de Calidon", "derrotado_por": "Atalanta","descripcion":"","capturada_por": ""},
{"nombre": "Carcinos", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Gerion", "derrotado_por": "Heracles","descripcion":"","capturada_por": ""},
{"nombre": "Cloto", "derrotado_por": "Zeus","descripcion":"","capturada_por": ""},
{"nombre": "Laquesis", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Atropos", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Minotauro de Creta", "derrotado_por": "Teseo","descripcion":"","capturada_por": ""},
{"nombre": "Harpias", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Argos Panoptes", "derrotado_por": "Hermes","descripcion":"","capturada_por": ""},
{"nombre": "Aves del Estinfalo", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Talos", "derrotado_por": "Medea","descripcion":"","capturada_por": ""},
{"nombre": "Sirenas", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Piton", "derrotado_por": "Apolo","descripcion":"","capturada_por": ""},
{"nombre": "Cierva de Cerinea", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Basilisco", "derrotado_por": "","descripcion":"","capturada_por": ""},
{"nombre": "Jabali de Erimanto", "derrotado_por": "","descripcion":"","capturada_por": ""}
]

for criatura in criaturas:
    arbol.insert_node(criatura["nombre"], criatura)

#a. Listado inorden de las criaturas y quienes las derrotaron
print("----------Barrido inorden:----------") 
arbol.inorden()
print()

#b. se debe permitir cargar una breve descripción sobre cada criatura;
arbol.agregar_descripcion("Medusa", "Mujer con cabello de serpientes")
buscado = "Medusa"
pos = arbol.search(buscado)
if pos:
    print ("----------Información de la criatura:",buscado," ",pos.other_value)
print()


#c. mostrar toda la información de la criatura Talos;
buscado = "Talos"
pos = arbol.search(buscado)
if pos:
    print ("----------Información de la criatura:",buscado," ",pos.other_value)
print()

#d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
#arbol.contar_heroes(dic)

for criatura in criaturas:
    if criatura["derrotado_por"]:
        print(f'{criatura["nombre"]} fue derrotado por {criatura["derrotado_por"]}')
    else:
        print(f'{criatura["nombre"]} no fue derrotado por nadie')

heroes ={}
for criatura in criaturas:
    heroe = criatura["derrotado_por"]  # Obtener el héroe que derrotó a la criatura
    if heroe:  # Solo contamos si el héroe derrotó a la criatura
        if heroe in heroes:
            heroes[heroe] += 1  # Incrementamos el contador si ya existe el héroe
        else:
            heroes[heroe] = 1  # Iniciamos el contador para un nuevo héroe

arbol_heroes = BinaryTree()
for heroe in heroes:
    arbol_heroes.insert_node(heroe)
print(heroes)

lista = sorted(heroes.items(), key=lambda x: x[1], reverse=True)
top_3_heroes = lista[:3]
for heroe, derrotas in top_3_heroes:
    print(f'{heroe} (derrotó a {derrotas} criatura(s))')

print()

#g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo;
#arbol.agregar_captura("Cerbero", "Hades")


#h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó;
def capturar_por_heracles(self):
    criaturas = ["Cerbero", "Toro de Creta", "Cierva de Cerinea", "Jabali de Erimanto"]
    for criatura in criaturas:
        self.agregar_captura(criatura, "Heracles")
print()


#i. se debe permitir búsquedas por coincidencia (proximidad)
print("----------búsquedas por coincidencia: ")
arbol.buscar_por_coincidencia("T")

#j. eliminar al Basilisco y a las Sirenas;
arbol.delete_node("Basilisco")
arbol.delete_node("Sirenas")
print()

print("----------Barrido sin los nodos de Basilisco y Sirenas")
arbol.inorden()
print()

#k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias;
buscado = "Aves del Estinfalo"
pos = arbol.search(buscado)
if pos:
    derrota = input("------Ingrese el nombre de quien derroto a las Aves del Estinfalo: ")
    x=pos.other_value
    arbol.delete_node(buscado)
    x["derrotado_por"] = derrota
    arbol.insert_node(buscado,x)
print()

print("Barrido modificando quien derroto a las Aves del Estinfalo")
arbol.inorden()
print()

#l. modifique el nombre de la criatura Ladón por Dragón Ladón;
buscado = "Ladon"
pos = arbol.search(buscado)

if pos:
    nuevo_nombre = input("Ingrese el nuevo nombre de Ladon: ")
    bestia = pos.other_value
    arbol.delete_node(buscado)
    bestia["nombre"] = nuevo_nombre
    arbol.insert_node(nuevo_nombre,bestia)
print()


#m. realizar un listado por nivel del árbol
print("Barrido por nivel:")
arbol.by_level()
print()

#n. muestre las criaturas capturadas por Heracles.
print("Capturados por Heracles: ")
arbol.criaturas_capturadas("Heracles")