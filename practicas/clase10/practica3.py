archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/datos.txt","r")

lineas=archivo.readlines()

print(lineas)

for linea in lineas:
    print(linea.strip())

archivo.close()