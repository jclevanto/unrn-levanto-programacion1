clave_almacenada = "1234"
uso_clave_token = bool(input("Usa clave token? [S/n]: ")=="S")
clave_ingresada=""

if not uso_clave_token:
    clave_ingresada = input("Ingrse su clave: ")

if clave_almacenada==clave_ingresada:
    print("Acceso con clave")
elif uso_clave_token:
    print("Acceso permitido")
else:
    print("Acceso denegado")
