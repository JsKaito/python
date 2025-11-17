while True:
    nota = float(input("Escribe tu nota: "))
    if 0 <= nota <= 10:
        break
    print("Error: La nota debe estar entre 0 y 10. Inténtalo otra vez.")

if nota < 3:
    print("Muy Deficiente")
elif nota < 5:
    print("Insuficiente")
elif nota < 6:
    print("Suficiente")
elif nota < 7:
    print("Bien")
elif nota < 9:
    print("Notable")
elif nota <= 10:
    print("Sobresaliente")