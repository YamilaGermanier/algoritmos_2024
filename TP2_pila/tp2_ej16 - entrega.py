"""
16. Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. Desarrollar un algoritmo que
permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en ambos
episodios.
"""
from tp2_pila import Stack

p_empire = Stack()
p_force = Stack()
p_inter = Stack()
p_aux = Stack()

empire = ['Luke Skywalker', 'Leia Organa','R2-D2', 'C-3PO', 'Han Solo', 'Chewbacca', 'Lando Calrissian',  
           'Yoda', 'Boba Fett','Obi-Wan Kenobi', 'Darth Vader',]

force = ['Leia Organa', 'Luke Skywalker', 'Han Solo', 'Kylo Ren', 'Rey', 'Finn', 'Chewbacca', 
           'R2-D2', 'C-3PO', 'Poe Dameron']

for element in empire:
    p_empire.push(element)

for element in force:
    p_force.push(element)

# control de carga
print(p_empire.on_top())
print(p_force.on_top())

print("----------------------------------------------------------------")

### mientras haya elementos en ambas asignar variable y si son iguales cargo la intersección
while p_empire.size()>0:
    V = p_empire.pop()
    while p_force.size()>0:
        VII = p_force.pop()

        if (V == VII):
            p_inter.push(V)
        else:
            p_aux.push(VII)
        
    while p_aux.size()>0:
        p_force.push(p_aux.pop())


#  mostrar las coincidencias
def show(p_inter):
    while p_inter.size()>0:
        data = p_inter.pop()
        print(data)

print("Las coincidencias son:")
show(p_inter)
