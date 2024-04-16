# Desarrollar un algoritmo que permita calcular la siguiente serie:

# sumatorio 1/n + (1/n+1)
def sumatoriaSerie(num):
    if num == 1:
        return 1/num
    else:
        return 1/num + sumatoriaSerie(num-1)
    
print(sumatoriaSerie(2))