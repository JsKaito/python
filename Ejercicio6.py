pr = int(input("Ingrese el precio real del producto: "))
po = int(input("Ingrese el precio de oferta del producto: "))
desc= 100*((pr-po)/pr)
print("El descuento es de", desc,"%")