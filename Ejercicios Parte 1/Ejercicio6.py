pr = float(input("Ingrese el precio real del producto: "))
po = float(input("Ingrese el precio de oferta del producto: "))
desc= 100*((pr-po)/pr)
print(f"El descuento es de {desc} %")