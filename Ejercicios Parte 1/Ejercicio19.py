banco = 1000
efectivo = 3000

barra = "\n-------------------------------"

while True:
    
    print(
        barra,
        "\nBienvenido a su Cajero Virtual",
        barra,
        f"\nTu saldo es {banco}, y tienes {efectivo} en efectivo.",
        barra,
        "\n1. Ingresar dinero en cuenta",
        "\n2. Retirar dinero de la cuenta",
        "\n3. Salir",
        barra
    )
    num = int(input("Escribe una opción: "))
    print()
    
    if num == 1: # Depositar
        cantidad = int(input("Introduce la cantidad a depositar: "))
        if efectivo < cantidad:
            print("No tienes dinero en efectivo suficiente.")
        else:
            banco += cantidad
            efectivo -= cantidad
            print("Depósito realizado.")
    
    elif num == 2: # Retirar
        cantidad = int(input("Introduce la cantidad a retirar: "))
        if cantidad < banco:
            print("No tienes dinero suficiente en tu cuenta.")
        else:
            banco -= cantidad
            efectivo += cantidad
            print("Retirada realizada.")
            
    elif num == 3: # Salir
        break
    
    else: # Opción errónea
        print("No se ha introducido ninguna opción correcta.")
        
print("Gracias por usar nuestro cajero.")