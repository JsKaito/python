import random

dados = [0, 0, 0]

def tirarDados(dados):
    for i in range(len(dados)):
        dados[i] = random.randint(1, 6)
    return dados

def calcResultado(dados):
    cont = 0
    
    for i in range(len(dados)):
        if dados[i] == 6:
            cont += 1
    
    if cont == 3:
        return "¡Excelente!"
    elif cont == 2:
        return "¡Muy bien!"
    elif cont == 1:
        return "¡Regular!"
    elif cont == 0:
        return "¡Pésimo!"

tirarDados(dados)    
calcResultado(dados)

print(calcResultado(dados),"Tus resultados han sido:", dados)


'''
Función para testear si la lógica es correcta que he usado para testear (Mira cuantas tiradas tarda en sacar triple 6):

    tiradas = 0

    while not dados == [6, 6, 6]:
        tirarDados(dados)
        tiradas += 1
        
    print(tiradas)

'''