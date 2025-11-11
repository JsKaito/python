fact = 1
n = int(input("Escribe un número positivo: "))

for i in range(1, n+1):
    fact *= i
    
print("El factorial es", fact)