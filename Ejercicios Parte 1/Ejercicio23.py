precio = 100 # Precio del producto (cambiable)

while True:
    print("\n¿Cómo desea pagar?",
          "\n1. Tarjeta (3% de recargo)",
          "\n2. Efectivo (5% de descuento)")
    opc = int(input("\nElige una opción: "))
    
    if opc == 1:
        tarjeta = True
        break
    
    elif opc == 2:
        tarjeta = False
        break
    
    print("Introduce una opción correcta.")

if tarjeta == True:
    precio += precio * 0.03
elif tarjeta == False:
    precio -= precio * 0.05

print(f"\nEl precio final es de {precio:.2f} euros.") # 2f para mostrar 2 decimales como en los precios reales