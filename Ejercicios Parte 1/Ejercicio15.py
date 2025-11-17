n1 = float(input("Escribe el primer número: "))
n2 = float(input("Escribe el segundo número: "))
n3 = float(input("Escribe el tercer número: "))

if n1 == n2 == n3:
    print("Los tres números son iguales.")
elif n1 == n2:
    print("El número 1 y el número 2 son iguales. El número mayor es", max(n1, n3), "y el menor es", min(n1, n3))
elif n1 == n3:
    print("El número 1 y el número 3 son iguales. El número mayor es", max(n1, n2), "y el menor es", min(n1, n2))
elif n2 == n3:
    print("El número 2 y el número 3 son iguales. El número mayor es", max(n2, n1), "y el menor es", min(n2, n1))
else:
    print("El número mayor es", max(n1, n2, n3), "y el menor es", min(n1, n2, n3))