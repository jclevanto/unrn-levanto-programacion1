clave_almacenada = "1234"
clave_ingresada=""
uso_clave_token = bool(input("Usa clave token? [S/n]: ")=="S")

if not uso_clave_token:
    clave_ingresada = input("Ingrse su clave: ")

if clave_almacenada==clave_ingresada or uso_clave_token:
    print("Acceso permitido")
else:
    print("Acceso denegado")
