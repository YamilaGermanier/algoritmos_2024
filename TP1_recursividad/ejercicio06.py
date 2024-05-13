# Dada una secuencia de caracteres, obtener dicha secuencia invertida.

# unacadena = anedacanu
def invertida(cadena):
    if len(cadena) == 0: #longitud
        return cadena
    else:
        return cadena[-1] + invertida(cadena[:-1]) # -1 último elemento + función menos el último elemnto
cadena='hola'
print(invertida(cadena))