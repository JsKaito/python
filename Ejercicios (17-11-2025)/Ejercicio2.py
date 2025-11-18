altura = int(input("Introduce la altura de la escalera: "))
for i in range (1, altura+1):
    if i == 1:
        print('4'*i)
    elif i == altura:
        print('4'*i)
    else:
        print('4' + ' '*(i-2) + '4')