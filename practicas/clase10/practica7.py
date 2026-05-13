archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/nombres.txt","r")

nombres=[]

for nombre in archivo.readlines():
    nombres.append(nombre.strip())

archivo.close()
for i in range (len(nombres)):
    print(f"{i}: {nombres[i]}")