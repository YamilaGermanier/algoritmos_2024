from random import randint, choice


def hash_legion(value):
    return trooper[:2]

def hash_numerica(value):
    return trooper[-3:]


legiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FO']

tabla_legiones = {}
table_numerica = {}

for legion in legiones:
    tabla_legiones[legion] = []



for i in range(0, 20):
    trooper = f'{choice(legiones)}-{randint(1000, 9999)}'
    clave = hash_numerica(trooper)
    if clave not in table_numerica:
        table_numerica[clave] = []

    table_numerica[clave].append(trooper)
    tabla_legiones[hash_legion(trooper)].append(trooper)

print(tabla_legiones)
#print(table_numerica)
print("------------------------------------------")

#! C FN-2187 traitor
list_187 = table_numerica.get('187', []) #saco primero todos los trooper que terminan en 187 y los pongo en otra lista
if 'FN-2187' in list_187: # reviso si el traidor está en la lista
    pos_fn_2187 = list_187.index('FN-2187') # variable para la posición del trooper si este está en la lista
    if pos_fn_2187 > -1:
        print(f'esta en la posicion {pos_fn_2187}')
else:
    print('no esta')
print(len(list_187))
print()

#! D mission_assault 781 mission_explore 537

# mission_assault = table_numerica.get('781', [])
# print('Stromtroopers para mision de asalto')
# for index, trooper in enumerate(mission_assault):
#     print(f'{index} - {trooper}')
# print()
# mission_explore = table_numerica.get('537', [])
# print('Stromtroopers para mision de exploración')
# for index, trooper in enumerate(mission_explore):
#     print(f'{index} - {trooper}')
# print()

#! E hoth CT endor TF
# mission_hoth = tabla_legiones.get('CT', [])
# print('Stromtroopers para mision a hoth')
# for index, trooper in enumerate(mission_hoth):
#     print(f'{index} - {trooper}')
# print()
# mission_endor = tabla_legiones.get('TF', [])
# print('Stromtroopers para mision a hoth')
# for index, trooper in enumerate(mission_endor):
#     print(f'{index} - {trooper}')
# print()