ruta = "minitp8/Ejercicio3/"
archivo = open(ruta + "nombres.txt","w")

nombres=[]

for i in range(4):
    nombre=input(f"Ingrese el nombre numero {i+1}/4: ")
    if nombre == "":
        print("Nombre vacio")
    else:
        nombres.append(nombre)
print(nombres)

for nombre in nombres:
    archivo.write(nombre + "\n")
archivo.close() 