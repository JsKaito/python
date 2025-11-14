horas = int(input("Escribe las horas trabajadas: "))
tarifa = float(input("Escribe la tarifa: "))


def calcularSalario(horas, tarifa):
    
    dinero = 0
    impuesto = 0
    
    if horas <= 35:
        dinero += horas * tarifa
    else:
        dinero += 35 * tarifa # Error del profesor
        horas -= 35
        dinero += horas * tarifa * 1.5
        
    if dinero > 500:
        excede = dinero - 500
        
        if excede > 400:
            impuesto1 = 400 * 0.25
            excede -= 400
        
        impuesto2 = excede * 0.45
        impuesto += impuesto1 + impuesto2
    
    return dinero - impuesto
        
print("El trabajador recibirá un total de",calcularSalario(horas, tarifa), "euros netos.")