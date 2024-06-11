def bernstein(cadena):
    """ Función hash de bernstein para cadenas """
    h=0
    for caracter in cadena:
        h = h * 33 + ord(caracter) # ord(caracter) permite conocer el valor numérico Unicode de un carácter específico.
    return h


print(bernstein("hola"))
print(bernstein("holi"))
print(bernstein("holis"))
print(bernstein("holu"))