neg, pos = 0, 0

while True:
    num = int(input("Escribe un número entero: "))
        
    if num < 0:
        neg +=1
        
    elif num > 0:
        pos +=1
        
    elif num == 0:
        break

print("Números positivos:", pos, "\n"
      "Números negativos:", neg)