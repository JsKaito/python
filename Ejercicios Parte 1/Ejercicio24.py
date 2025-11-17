descuento = 0

while True:
    precio = float(input("Escribe el precio total de la compra: "))
    if precio > 0:
        break
    
    print("El precio debe ser un valor positivo.")
    
while True:
    print("\n1. Lunes",
          "\n2. Martes",
          "\n3. Miércoles",
          "\n4. Jueves",
          "\n5. Viernes",
          "\n6. Sábado",
          "\n7. Domingo")
    
    dia = int(input("\nEscribe el día de la semana (1-7): "))
    if 1 <= dia <= 7:
        break
    
    print("El día debe estar entre 1 y 7.")

if dia in [2, 4]: # Si es martes o jueves
    descuento = 15

precio -= precio * (descuento / 100)

print(f"\nEl precio final de la compra es {precio:.2f}€. Se te ha descontado un {descuento}%.")    