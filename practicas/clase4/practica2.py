contrasena_registrada = "1234"
contrasena_correcta = False

while(not contrasena_correcta):
    contrasena_ingresada = input("Ingrese su contrasenia: ")

    if (contrasena_registrada==contrasena_ingresada):
        contrasena_correcta=True
    else:
        print("Contrasenia incorrecta")

print("Acceso permitido")
