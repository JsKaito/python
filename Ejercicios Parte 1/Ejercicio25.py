# Esta vez he decidido intentar usar un diccionario con triplas para optimizar el código.add(), usándolo como una especie de control switch.
# Es parecido pero con facultades en vez de días de la semana.

facultades = {
    1:("Ingeniería de Sistemas", 350, 650),
    2:("Derecho", 300, 550),
    3:("Ingeniería Naviera", 300, 500),
    4:("Ingeniería Pesquera", 310, 460),
    5:("Contabilidad", 280, 490),
    6:("Administración", 360, 520)
    }
    
nombre = str(input("Ingresa tu nombre: "))
    
print("\nFacultades:")
    
for numero, datos in facultades.items():
    print(f"{numero}. {datos[0]}") # Datos contiene el nombre, la matrícula y la mensualidad.
    
while True:
    num = int(input("\nIngresa tu facultad (1-6): "))
    if num in facultades:
        break
    
    print("Número de facultad incorrecto. Debe estar entre 1 y 6.")
    
facultad, matricula, mensualidad = facultades[num]
igv = (mensualidad + matricula) * 0.18

print(f"\n{nombre}, tu matrícula es de {matricula}, tu mensualidad de {mensualidad} y tu IGV es de {igv}.")

print(f"\nTu coste total es {matricula + mensualidad + igv} €")