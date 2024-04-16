# Desarrollar una función que permita convertir un número romano en un número decimal.

# ROMANOS I=1, V=5, X=10, L=50, C=100, D=500, M=1000
def translate(romanos):
    dico = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}

    romanos = romanos.upper()
    decimal = 0

    for romano in romanos[:-1]:
        if romano[-1]> romano[-2]:
            return decimal #???????????????????????????
