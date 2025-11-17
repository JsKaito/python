b500, b200, b100, b50, b20, b10, b5 = 0, 0, 0, 0, 0, 0, 0

while True:
    try:
        
        n = int(input("Introduce una cantidad en euros múltiplo de 5: "))
        if n % 5 != 0 or n < 0:
            print("Error. La cantidad debe ser positiva y múltiplo de 5.")
            continue
        break
    
    except ValueError:
        print("Error. Debes introducir un número entero.")

while True:
    if n >= 500:
        b500 += 1
        n -= 500
    elif n >= 200:
        b200 += 1
        n -= 200
    elif n >= 100:
        b100 += 1
        n -= 100
    elif n >= 50:
        b50 += 1
        n -= 50
    elif n >= 20:
        b20 += 1
        n -= 20
    elif n >= 10:
        b10 += 1
        n -= 10
    elif n >= 5:
        b5 += 1
        n -= 5
    elif n == 0:
        break
    
print("Cantidad de billetes")
print("Billetes de 500: ", b500)
print("Billetes de 200: ", b200)
print("Billetes de 100: ", b100)
print("Billetes de 50: ", b50)
print("Billetes de 20: ", b20)
print("Billetes de 10: ", b10)
print("Billetes de 5: ", b5)