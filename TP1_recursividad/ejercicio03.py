# 3. Implementar una función para calcular el producto de dos números enteros dados.

# 5*3= 5+5+5........... N*M= N*(M-1)

def producto(num1, num2):
    if num2 == 1:
        return num1
    else:
        return num1 + producto(num1, num2-1)
    

print(producto(5,10))