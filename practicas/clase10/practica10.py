archivo = open ("/workspaces/unrn-levanto-programacion1/practicas/clase10/mis_datos","w")

datos = ["Hola 1", "Hola 2", "Hola 4"]

archivo.writelines("\n".join(datos))

archivo.close()
