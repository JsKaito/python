def sumar(n1, n2):
    return n1 + n2

def restar(n1, n2):
    return n1 - n2

def multiplicar(n1, n2):
    return n1 * n2

def dividir(n1, n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "No se puede dividir entre 0."

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))

print(f"Suma: {sumar(n1, n2)} \n",
      f"Resta: {restar(n1, n2)} \n",
      f"Multiplicación: {multiplicar(n1, n2)} \n",
      f"División: {dividir(n1, n2)}")