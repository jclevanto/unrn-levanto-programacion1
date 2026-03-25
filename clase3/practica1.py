contrasena_correcta=1234
acceso=False

while(not acceso):

    contrasena_ingresada=int(input("Ingrese su contrasenia: "))

    if (contrasena_correcta==contrasena_ingresada):
        acceso=True
        print("Acceso permitido")
    else:
        print("Acceso denegado")

print("Gracias por usar nuestro sistema")