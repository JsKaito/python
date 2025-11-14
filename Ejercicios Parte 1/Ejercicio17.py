cuenta = ("kaito","hola123")

user = str(input("Escribe tu nombre de usuario: "))
if user == cuenta[0]:
    password = str(input("Escribe tu contraseña: "))
    if password == cuenta[1]:
        print("Inicio de sesión correcto.")
    else:
        print("Contraseña incorrecta.")
else:
    print("El usuario no existe.")