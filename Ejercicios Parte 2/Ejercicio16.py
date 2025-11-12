bandera = False
while True:
    nota = int(input("Escribe una nota entre 0 y 10: "))
    if nota == -1:
        break;
    elif nota < 0 or nota > 10:
        print("La nota debe estar entre 0 y 10. Si quieres terminar, introduce '-1'.")
    elif nota == 10:
        bandera = True
print("Ha habido al menos un 10.") if bandera else print("No ha habido ningún 10.")