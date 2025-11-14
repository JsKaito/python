while True:
    
    tiempo = input("\nIntroduce un tiempo (hh:mm:ss): ")
    
    try:
        hora, minuto, segundo = map(int, tiempo.split(":"))
    
        if (0 <= hora <= 23) and (0 <= minuto <= 59) and (0 <= segundo <= 59):
            break
        else:
            print("Introduce un rango horario correcto. Los rangos son: Horas: 0-23, Minutos: 0-59, Segundos: 0-59.")
            
    except ValueError: # Para que no crashee si no se introduce (hh:mm:ss)
        print("Introduce el formato adecuado, por favor.")
        continue

segundo += 1

if segundo > 59:
    segundo = 0
    minuto += 1

if minuto > 59:
    minuto = 0
    hora += 1

if hora > 23:
    hora = 0
    
print(f"La hora en un segundo será {hora:02}:{minuto:02}:{segundo:02}") # El 02 es para que muestre 0 a la izquierda si es necesario.