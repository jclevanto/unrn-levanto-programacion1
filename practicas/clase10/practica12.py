nombres=[]
documentos=[]

for i in range (5):
    nombres.append(input("Ingrese un nombre: "))
    documentos.append(int(input("Ingrese un DNI: ")))

archivo = open ("/workspaces/unrn-levanto-programacion1/practicas/clase10/nombres_documentos.csv","w")

for i in range (5):
    archivo.write(f"{nombres[i]}, {documentos[i]}\n")
archivo.close()