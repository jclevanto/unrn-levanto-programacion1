clave_almacenada = "1234"
uso_clave_token = bool(input("Usa clave token? [S/n]: ")=="S")
clave_ingresada = input("Ingrse su clave: ")

if (clave_almacenada==clave_ingresada and uso_clave_token):
    print("Acceso permitido")
else:
    print("Acceso denegado")

print("Gracias por usar nuestro sistema")