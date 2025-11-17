# Si el programa tiene que decir si ha habido algún negativo al final:

iteraciones = 0
while iteraciones < 100:
    num = float(input("Escribe un número entero: "))
    
    if num != 0:
        iteraciones += 1
        
    if num < 0:
        flag = True

print("Se ha introducido un número negativo.") if flag else print("No se ha introducido ningún número negativo.")


# Si el programa tiene que decir el mensaje en el momento que se introduce el número negativo:

iteraciones = 0
while iteraciones < 100:
    num = float(input("Escribe un número entero: "))
    
    if num != 0:
        iteraciones += 1
        
    if num < 0:
        print("Se ha introducido un número negativo.")