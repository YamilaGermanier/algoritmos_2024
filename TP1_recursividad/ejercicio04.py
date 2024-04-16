# 4 - Implementar una función para calcular la potencia dado dos números enteros, el primero representa
#     la base y segundo el exponente.

# b^e | 2^3 = 2*2*2 | B^E = B * (B * (E-1))
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * (potencia(base, exponente-1))
    
print(potencia(2,10))