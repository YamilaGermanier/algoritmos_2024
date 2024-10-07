"""
Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic Universe
(MCU), desarrollar un algoritmo que contemple lo siguiente:
    a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo booleano
    que indica si es un héroe o un villano, True y False respectivamente;
    b. listar los villanos ordenados alfabéticamente;
    c. mostrar todos los superhéroes que empiezan con C;
    d. determinar cuántos superhéroes hay el árbol;

    e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
    encontrarlo en el árbol y modificar su nombre;
    f. listar los superhéroes ordenados de manera descendente;

    g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes y otro a
    los villanos, luego resolver las siguiente tareas:
        I. determinar cuántos nodos tiene cada árbol;
        II. realizar un barrido ordenado alfabéticamente de cada árbol.
"""
from arbol_avl import BinaryTree

MCU = [
    {'nombre':'Black Widow', 'is_hero': True},
    {'nombre':'Doctor Strnge', 'is_hero': True},
    {'nombre':'Iron Man', 'is_hero': True},
    {'nombre':'Thanos', 'is_hero': False},
    {'nombre':'Kang', 'is_hero': False},
    {'nombre':'Captain Marvel', 'is_hero': True},
    {'nombre':'Agatha Harkness', 'is_hero': False},
    {'nombre':'Captain America', 'is_hero': True},
    {'nombre':'Scarlet Witch', 'is_hero': True},
    {'nombre':'Hela', 'is_hero': False},
]

arbol = BinaryTree()
arbol_heroes = BinaryTree()
arbol_villanos = BinaryTree()

for personaje in MCU:
    arbol.insert_node(personaje['nombre'], personaje) # por el arbol avl

# ---- PUNTO B ----#
print('Villanos ordenados alfabeticamente:')
arbol.inorden_villanos()
print()

# ---- PUNTO C ----#
print('Superheroes que empiezan con C')
arbol.inorden_superheros_start_with('C')
print()

# ---- PUNTO D ----#
print('En el arbol hay', arbol.contar_super_heroes(), 'heroes.')
print()

# ---- PUNTO E ---- #
buscado = input("Ingrese el nombre a buscar para modificar: ")
pos = arbol.search(buscado)
if pos:
    nuevo_nombre = input('Ingrese el nuevo nombre: ')
    
    superheroe = pos.other_value
    
    arbol.delete_node(buscado)
    
    superheroe['nombre'] = nuevo_nombre
    
    arbol.insert_node(nuevo_nombre, superheroe)
print()

# ---- PUNTO F ---- #
print('Superheroes ordenados de manera descendente:')
arbol.postorden()
print()

# ---- PUNTO G ---- #
arbol_heroes = arbol.separar_arbol(arbol_heroes, True)
print('Arbol de superheroes:')
arbol_heroes.inorden()
print('El arbol de superheroes tiene', arbol_heroes.contar_nodos(True), 'nodos.')
print()

arbol_villanos = arbol.separar_arbol(arbol_villanos, False)
print('Arbol de villanos:')
arbol_villanos.inorden()
print('El arbol de villanos tiene', arbol_villanos.contar_nodos(False), 'nodos.')
print()




