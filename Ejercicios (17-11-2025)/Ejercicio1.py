#altura = 5
altura = int(input("Introduce la altura de la escalera: "))

print(' '*altura, '*', sep='') # Punta alta

for i in range(1, altura+1):
    print(' '*(altura-i), '*', ' '*(i-1), '*', sep='') # Tríangulo alto (La última fila hace de punto medio y se corrige abajo)

for i in range(altura, 1, -1):
    print(' '*(altura+1 - i), '*', ' '*(i-2), '*', sep='') # Triángulo bajo
    
print(' '*altura, '*', sep='') #Punta baja