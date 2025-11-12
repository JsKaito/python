iteraciones, neg, pos = 0, 0, 0
while iteraciones < 5:
    num = int(input("Escribe un número entero: "))

    if num < 0:
        neg += 1
        iteraciones += 1
        
    elif num > 0:
        pos += 1
        iteraciones += 1

print("Se han introducido", pos, "números positivos y", neg, "números negativos.")