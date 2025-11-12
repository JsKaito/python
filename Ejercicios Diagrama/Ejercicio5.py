import math

r = int(input("Ingrese el radio: "))
l = 2 * math.pi * r
a = math.pi * r**2
vol = (4/3) * math.pi * r**3
print("La longitud de la circunferencia es", l, "\n"
      "El área del círculo es", a, "\n"
      "El volumen de la esfera es", vol)