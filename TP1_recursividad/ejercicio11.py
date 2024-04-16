# Desarrollar un algoritmo que invierta un número entero sin 
# convertirlo a cadena


def invertir(numero):
    if numero < 10:
        return numero
    else:
        return (numero%10)* (10**len(str(numero//10))) + invertir(numero//10) 

print(invertir(705))