contrasena_correcta=1234

for i in range (0, 3):
    contrasena_ingresada=int(input("Ingrese su contrasenia: "))
    if (contrasena_correcta==contrasena_ingresada):
        print("Acceso permitido")
        break
    else:
        print(f"Acceso denegado, le quedan {2-i} intento/s")

print("Gracias por usar nuestro sistema")

#ctrl + k + c comenta todo
