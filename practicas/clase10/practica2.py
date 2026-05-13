archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/datos.txt","r")
# contenido = archivo.read()

# print(contenido, end ="")
linea = archivo.readline()

print(linea.strip())

archivo.close