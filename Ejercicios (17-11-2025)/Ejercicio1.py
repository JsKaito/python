altura = int((input("Introduce la altura de la mitad de la pirámide horizontal. El número debe ser impar: ")))//2

# Mitad Superior
for i in range (1, altura + 1):
    
    if i == 1:
        print(' ' * (altura), '*', sep= '') # Punta alta
    else:
        print(' ' * (altura - i +1), '*', (i-2) * ' ', '*', sep ='') # Resto del triángulo

# Conexión
print('*', ' ' * (altura - 1), '*', sep = '')

# Mitad Inferior
for i in range (altura, 0, -1): # Invierto el bucle por completo, pasando del rango (1, altura + 1), subiendo a (altura, 1-1), bajando.
    
    if i == 1:
        print(' ' * (altura), '*', sep= '') # Punta baja
    else:
        print(' ' * (altura - i +1), '*', (i-2) * ' ', '*', sep ='') # Resto del triángulo