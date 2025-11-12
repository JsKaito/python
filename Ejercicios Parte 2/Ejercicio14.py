altura = int(input("Introduce la altura de la pirámide: "))
for i in range(1, altura + 1):
    #print(" "*i,"*" * i," "*i)
    print((altura-i)*" ", (i*2-1)*"*")