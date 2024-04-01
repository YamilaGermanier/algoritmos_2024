# 1 - Implementar una función que permita obtener el valor en la sucesión de Fibonacci para un número dado.

# 1 1 2 3 5 8 13... n=n-1 + n-2
def fibonacci(num):
    if num == 1 or num == 0:
        return num
    else:
        return fibonacci(num-1) + fibonacci(num-2)
     

num=8

print(fibonacci(num))
