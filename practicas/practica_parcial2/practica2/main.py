ruta = "/workspaces/unrn-levanto-programacion1/practicas/practica_parcial2/practica2/"

# Abra el archivo en modo lectura.
# Lea las líneas del archivo.
# Separe cada línea usando split(";").
# Cuente cuántos accesos fueron permitido.
# Guarde en una lista los nombres con acceso permitido.
# Ignore los estados que no sean permitido o denegado.
# Muestre la cantidad de accesos permitidos y la lista final.

archivo=open(ruta+"archivo.txt","r")

permitidos=[]
lineas = archivo.readlines()
print(lineas)

for linea in lineas:
    nombre, accion = linea.split(";")
    accion = accion.strip("\n")
    if accion == "permitido":
        permitidos.append(nombre)

print(f"Hubo {len(permitidos)} permitidos y fueron: {permitidos}")