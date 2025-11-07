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

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))

print("Suma:", sumar(n1, n2), "\n"
      "Resta:", restar(n1, n2), "\n"
      "Multiplicación:", multiplicar(n1, n2), "\n"
      "División:", dividir(n1, n2))