# Desarrollar un algoritmo que cuente la cantidad de dígitos de un número entero



def contador(num):
    if num < 10:
         return 1
    else:
         return 1 + contador(num//10)

print(contador(100))