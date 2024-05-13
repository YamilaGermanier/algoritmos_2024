# Desarrollar un algoritmo que permita convertir un número entero en sistema decimal a sistema
# binario.

# entero decimal / 2 = resto
def entero_binario(entero):
   
    if entero <= 1:
        return str(entero)
    else:
        return entero_binario(entero // 2) + str(entero%2) # convierto a cadena con 'str()'
    
print(entero_binario(13))

