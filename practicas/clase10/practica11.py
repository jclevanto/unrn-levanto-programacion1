nombres=[]

for i in range (5):
    nombres.append(input("Ingrese un nombre: "))

archivo = open ("/workspaces/unrn-levanto-programacion1/practicas/clase10/nombres.txt","w")

archivo.writelines("\n".join(nombres))

archivo.close()