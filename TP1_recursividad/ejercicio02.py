# 2. Implementar una función que calcule la suma de todos los números enteros comprendidos 
#    entre cero y un número entero positivo dado.

# 0 + 1 + 2 + 3 + 4 + 5 + 6 = result | 6 + sum5 | 5 + sum4
def sumatoria(num):
    if num == 0:
        return num
    else:
        return num + sumatoria(num-1)
    
num=10
print(sumatoria(num))