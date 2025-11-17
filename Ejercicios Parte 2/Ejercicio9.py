neg, pos = 0, 0

while True:
    num = float(input("Escribe un número: "))
        
    if num < 0:
        neg +=1
        
    elif num > 0:
        pos +=1
        
    elif num == 0:
        break

print("Números positivos:", pos, "\n"
      "Números negativos:", neg)