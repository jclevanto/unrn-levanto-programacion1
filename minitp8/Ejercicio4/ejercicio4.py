ruta = "minitp8/Ejercicio4/"
archivo = open(ruta+"temperaturas.txt","r")

temperaturas={}

for datos in archivo:
    datos=datos.split(";")
    datos[1]=datos[1].strip("\n")
    if not datos[0] in temperaturas:
        temperaturas[datos[0]]=[]
    temperaturas[datos[0]].append(datos[1])
print(temperaturas)
