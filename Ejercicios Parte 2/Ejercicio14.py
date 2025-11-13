altura = int(input("Introduce la altura de la pirámide: "))
for i in range(1, altura + 1):
    print((altura-i)*" ", (i*2-1)*"*") # (altura-i) son los espacios, (cada vez menos); (i*2-1) son los asteriscos (cada vez más pero impares)