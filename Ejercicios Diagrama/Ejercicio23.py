# Versión 1

neg, pos = 0, 0
num = -1

while num != 0:
    num = float(input("Escribe un número entero: "))
        
    if num < 0:
        neg +=1
        
    elif num > 0:
        pos +=1

print("Números positivos:", pos, "\n"
      "Números negativos:", neg)


# Versión 2 (Más eficiente)

neg, pos = 0, 0

while True:
    num = float(input("Escribe un número entero: "))
        
    if num < 0:
        neg +=1
        
    elif num > 0:
        pos +=1
        
    elif num == 0:
        break

print("Números positivos:", pos, "\n"
      "Números negativos:", neg)