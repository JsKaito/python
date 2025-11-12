n1 = int(input("Escribe el primer número: "))
n2 = int(input("Escribe el segundo número: "))

if n1 < n2:
    print(n1, "<", n2)
elif n2 < n1:
    print(n2, "<", n1)
elif n1 == n2:
    print("Los números son iguales.")