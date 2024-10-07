from typing import Counter
from cola import Queue

class BinaryTree:

    class __Node:
        def __init__(self, value, left=None, right=None, other_value=None):
            self.value = value
            self.left = left
            self.right = right
            self.other_value = other_value
            self.height = 0

    def __init__(self):
        self.root = None

    def height(self, root):
        if root is None:
            return -1
        else:
            return root.height

    def update_height(self, root):
        if root is not None:
            # print(f'actualizar altura de {root.value}')
            left_height = self.height(root.left)
            right_height = self.height(root.right)
            root.height = max(left_height, right_height) + 1
            # print(f'altura left {left_height} altura right {right_height}')
            # print(f'altura de {root.value} es {root.height}')

    def simple_rotation(self, root, control):
        if control:
            aux = root.left
            root.left = aux.right
            aux.right = root
        else:
            aux = root.right
            root.right = aux.left
            aux.left = root
        self.update_height(root)
        self.update_height(aux)
        root = aux
        return root

    def double_rotation(self, root, control):
        if control:
            root.left = self.simple_rotation(root.left, False)
            root = self.simple_rotation(root, True)
        else:
            root.right = self.simple_rotation(root.right, True)
            root = self.simple_rotation(root, False)
        return root

    def balancing(self, root):
        if root is not None:
            if self.height(root.left) - self.height(root.right) == 2:
                #print('desbalanceado a la leftuierda')
                if self.height(root.left.left) >= self.height(root.left.right):
                    #print('rotar simple derecha')
                    root = self.simple_rotation(root, True)
                else:
                    #print('rotar doble derecha')
                    root = self.double_rotation(root, True)
            elif self.height(root.right) - self.height(root.left) == 2:
                #print('desbalanceado a la derecha')
                if self.height(root.right.right) >= self.height(root.right.left):
                    #print('rotar simple leftuierda')
                    root = self.simple_rotation(root, False)
                else:
                    #print('rotar doble leftuierda')
                    root = self.double_rotation(root, False)
        return root

    def insert_node(self, value, other_value=None):
        def __insert(root, value, other_value=None):
            if root is None:
                return BinaryTree.__Node(value, other_value=other_value)
            elif value < root.value:
                root.left = __insert(root.left, value, other_value)
            else:
                root.right = __insert(root.right, value, other_value)
            root = self.balancing(root)
            self.update_height(root)
            return root

        self.root = __insert(self.root, value, other_value)

    def search(self, key):
        def __search(root, key):
            if root is not None:
                if root.value == key:
                    # print('lo encontre')
                    return root
                elif key < root.value:
                    # print(f'buscalo a la leftuierda de {root.value}')
                    return __search(root.left, key)
                else:
                    # print(f'buscalo a la derecha de {root.value}')
                    return __search(root.right, key)
            # else:
            #     print('no hay nada')
        aux = None
        if self.root is not None:
            aux = __search(self.root, key)
        return aux

    def preorden(self):
        def __preorden(root):
            if root is not None:
                print(root.value)
                # print(f'leftuierda de {root.value}')
                __preorden(root.left)
                # print(f'derecha de {root.value}')
                __preorden(root.right)

        if self.root is not None:
            __preorden(self.root)

    def contar_super_heroes(self):
        def __contar_super_heroes(root):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') is True:
                    counter = 1
                counter += __contar_super_heroes(root.left)
                counter += __contar_super_heroes(root.right)
            return counter

        return __contar_super_heroes(self.root)

    def inorden(self):
        def __inorden(root):
            if root is not None:
                __inorden(root.left)
                print(root.value)
                __inorden(root.right)

        if self.root is not None:
            __inorden(self.root)

    def postorden(self):
        def __postorden(root):
            if root is not None:
                __postorden(root.right)
                print(root.value)
                __postorden(root.left)

        if self.root is not None:
            __postorden(self.root)

    def inorden_villanos(self):
        def __inorden_villanos(root):
            if root is not None:
                __inorden_villanos(root.left)
                if root.other_value.get('is_hero') is not True:
                    print(root.value)
                __inorden_villanos(root.right)

        if self.root is not None:
            __inorden_villanos(self.root)

    def inorden_superheros_start_with(self, start):
        def __inorden_superheros_start_with(root, start):
            if root is not None:
                __inorden_superheros_start_with(root.left, start)
                if root.other_value.get('is_hero') is True and root.value.startswith(start):
                    print(root.value)
                __inorden_superheros_start_with(root.right, start)

        if self.root is not None:
            __inorden_superheros_start_with(self.root, start)

    def by_level(self):
        pendientes = Queue()
        if self.root is not None:
            pendientes.arrive(self.root)

        while pendientes.size() > 0:
            node = pendientes.attention()
            print(f"nivel {node.height}", node.value)
            if node.left is not None:
                pendientes.arrive(node.left)
            if node.right is not None:
                pendientes.arrive(node.right)

    def delete_node(self, value):
        def __replace(root):
            if root.right is None:
                # print(f'no tiene derecha es el mayor {root.value}')
                return root.left, root
            else:
                # print('seguir buscando nodo par remplaz+ar a la dercha')
                root.right, replace_node = __replace(root.right)
                return root, replace_node

        def __delete(root, value):
            value_delete = None
            if root is not None:
                if root.value > value:
                    # print(f'buscar  a la leftuierda de {root.value}')
                    root.left, value_delete = __delete(root.left, value)
                elif root.value < value:
                    # print(f'buscar  a la derecha de {root.value}')
                    root.right, value_delete = __delete(root.right, value)
                else:
                    # print('valor encontrado')
                    value_delete = root.value
                    if root.left is None:
                        # print('a la leftuierda no hay nada')
                        return root.right, value_delete
                    elif root.right is None:
                        # print('a la derecha  no hay nada')
                        return root.left, value_delete
                    else:
                        # print('tiene ambos hijos')
                        root.left, replace_node = __replace(root.left)
                        root.value = replace_node.value
                        # return root, value_delete
                    root = self.balancing(root)
                    self.update_height(root)
            return root, value_delete

        delete_value = None
        if self.root is not None:
            self.root, delete_value = __delete(self.root, value)
        return delete_value
    
    def separar_arbol(self, new_tree, is_hero):
        def __separar_arbol(root, new_tree, is_hero):
            if root is not None:
                # Si el personaje es un héroe o un villano, según el parámetro, lo inserta en el nuevo árbol
                if root.other_value.get('is_hero') == is_hero:
                    new_tree.insert_node(root.value, root.other_value)
                __separar_arbol(root.left, new_tree, is_hero)
                __separar_arbol(root.right, new_tree, is_hero)
        __separar_arbol(self.root, new_tree, is_hero)
        return new_tree
    
    def contar_nodos(self, is_hero):
        def __contar_nodos(root, is_hero):
            counter = 0
            if root is not None:
                if root.other_value.get('is_hero') == is_hero:
                    counter = 1
                counter += __contar_nodos(root.left, is_hero)
                counter += __contar_nodos(root.right, is_hero)
            return counter

        return __contar_nodos(self.root, is_hero)

    ### ------------------23------------------------------------

    def agregar_descripcion(self, nombre_criatura, descripcion):
        nodo = self.search(nombre_criatura)
        if nodo:
            nodo.other_value["descripcion"] = descripcion

    def agregar_captura(self, nombre_criatura, capturador):
        nodo = self.search(nombre_criatura)
        if nodo:
            nodo.other_value["derrotada_por_por"] = capturador

    def inorden_derrotados(self):
        def __inorden_derrotados(root):
            if root is not None:
                __inorden_derrotados(root.left)
                derrotado_por = root.other_value.get("derrotado_por", "No derrotado")
                print(f'{root.value} - Derrotado por: {derrotado_por}')
                __inorden_derrotados(root.right)
        
        if self.root is not None:
            __inorden_derrotados(self.root)
    
    def top_derrotadores(self, top_n=3):
        derrotadores = Counter()

        def __contar_derrotadores(root):
            if root is not None:
                derrotado_por = root.other_value.get("derrotado_por")
                if derrotado_por:
                    derrotadores[derrotado_por] += 1
                __contar_derrotadores(root.left)
                __contar_derrotadores(root.right)

        __contar_derrotadores(self.root)
        for derrotador, count in derrotadores.most_common(top_n):
            print(f'{derrotador}: {count} criaturas derrotadas')

    def listar_derrotados_por(self, heroe):
        def __listar_derrotados_por(root, heroe):
            if root is not None:
                if root.other_value.get("derrotado_por") == heroe:
                    print(root.value)
                __listar_derrotados_por(root.left, heroe)
                __listar_derrotados_por(root.right, heroe)

        __listar_derrotados_por(self.root, heroe)

    def listar_no_derrotados(self):
        def __listar_no_derrotados(root):
            if root is not None:
                if not root.other_value.get("derrotado_por"):
                    print(root.value)
                __listar_no_derrotados(root.left)
                __listar_no_derrotados(root.right)

        __listar_no_derrotados(self.root)

    def buscar_por_coincidencia(self, texto):
        def __buscar_por_coincidencia(root, texto):
            if root is not None:
                if texto.lower() in root.value.lower():
                    print(f'{root.value} - {root.other_value}')
                __buscar_por_coincidencia(root.left, texto)
                __buscar_por_coincidencia(root.right, texto)

        __buscar_por_coincidencia(self.root, texto)

    def eliminar_criaturas(self):
        criaturas = ["Basilisco", "Sirenas"]
        for criatura in criaturas:
            self.delete_node(criatura)

    def criaturas_capturadas(self, heroe):
        def __criaturas_capturadas(root, heroe):
            if root is not None:
                if root.other_value.get("capturada_por") == heroe:
                    print(root.value)
                __criaturas_capturadas(root.left, heroe)
                __criaturas_capturadas(root.right, heroe)

        __criaturas_capturadas(self.root, heroe)





#tree = BinaryTree()

# tree.insert_node('B')
# tree.insert_node('W')
# tree.insert_node('V')
# tree.insert_node('I')
# tree.insert_node('M')
# tree.insert_node('R')
# tree.insert_node('Z')
# tree.root = tree.balancing(tree.root)
#for i in range(1, 16):
 #   tree.insert_node(i)
  #  tree.by_level()
   # a = input()


#print('diferencia de altura', tree.height(tree.root.right) - tree.height(tree.root.left))
# tree.insert_node(19)
# tree.insert_node(7)
# tree.insert_node(31)
# tree.insert_node(11)
# tree.insert_node(10)
# tree.insert_node(45)
# tree.insert_node(22)
# tree.insert_node(27)

# pos = tree.search(27)
# if pos:
#     print('lo encontre', pos.value)
# else:
#     print('no esta')

# tree.delete_node(7)
# tree.delete_node(11)
# tree.delete_node(31)
# tree.delete_node(27)
# tree.delete_node(45)
# tree.delete_node(22)
# tree.delete_node(19)
# tree.delete_node(10)
# tree.insert_node(27)

# print(tree.delete_node(100))
# tree.preorden()

# print(tree.root.right)

# tree.by_level()