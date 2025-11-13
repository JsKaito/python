pares = impares = 0

for i in range (100, 201):
    if i % 2 == 0:
        pares += i
    elif i % 2 != 0:
        impares += i
    
print("La suma de los pares es", pares, "\nLa suma de los impares es", impares)