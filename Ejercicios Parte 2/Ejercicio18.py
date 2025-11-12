num = int(input("Introduce el número a elevar: "))
exponente = int(input("Introduce el exponente: "))
for i in range (exponente - 1):
    num *= num
print("El resultado es", num)