while True:
    numero = int(input("Escribe un número entre 0 y 99999: "))
    if 0 <= numero <= 99999:
        break
    
    print("Número inválido. Inténtalo de nuevo.")
print(f"El número tiene {len(str(numero))} cifras.")