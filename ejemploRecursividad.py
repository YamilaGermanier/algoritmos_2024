# recursividad

#factorial de 5
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n=5
print(factorial(n))