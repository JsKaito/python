limiteInferior, limiteSuperior = 1, 100
intentos = 0

print(f"\nPiensa un número entero entre {limiteInferior} y {limiteSuperior}.")
print("Introduce '0' si acierto, '1' si tu número es menor o '2' si es mayor.")

while True:
    guess = (limiteInferior + limiteSuperior) // 2
    
    print ("\n[0] Acierto | [1] Menor | [2] Mayor")
    opc = int(input(f"¿Tu número es {guess}? "))
    intentos += 1

    if opc == 0: # Si es acierto
        break
    
    elif opc == 1: # Si es menor
        limiteSuperior = guess - 1
        
    elif opc == 2: # Si es mayor
        limiteInferior = guess + 1
        
    else: # Si no es válido
        print("Opción no válida.")

print(f"He adivinado el número en {intentos} intentos.")