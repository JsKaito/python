from math import pi

r = float(input("Ingrese el radio: "))
l = 2 * pi * r
a = pi * r**2
vol = (4/3) * pi * r**3
print(f"La longitud de la circunferencia es {l} \n"
      f"El área del círculo es {a} \n"
      f"El volumen de la esfera es {vol}")