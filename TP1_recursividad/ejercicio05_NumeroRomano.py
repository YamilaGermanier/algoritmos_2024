# Desarrollar una función que permita convertir un número romano en un número decimal.

# ROMANOS I=1, V=5, X=10, L=50, C=100, D=500, M=1000
romanos = {
        'I':1, 
        'V':5, 
        'X':10, 
        'L':50, 
        'C':100, 
        'D':500, 
        'M':1000
    }

num_rom = input("Ingrese el rúmero romano: ")
num_rom = num_rom.upper() # los paso a mayúscula para que quede más lindo

def translate(num_rom):
    
    if len(num_rom)==1: #cuando queda 1
        return romanos[num_rom]

    elif (romanos[num_rom[0]] >= romanos[num_rom[1]]): # si actual >= que siguiente
        return romanos[num_rom[0]] + translate(num_rom[1:]) # sumo y  llamo a la función
    
    else: 
        return - romanos[num_rom[0]] + translate(num_rom[1:]) # si actual < que siguiente, resto y llamo a la función
    
print((f'El número romano {num_rom} equivale en decimal al número: '), translate(num_rom))

