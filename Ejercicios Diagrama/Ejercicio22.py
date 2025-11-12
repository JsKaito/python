neg = pos = iteraciones = 0
while iteraciones < 2:
    num = int(input("Escribe un número entero: "))
    
    if num != 0:
        iteraciones += 1
        
    if num < 0:
        neg +=1
        
    if num > 0:
        pos +=1

print("Números positivos:", pos, "\n"
      "Números negativos:", neg)