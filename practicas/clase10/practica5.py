archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/numeros.txt","r")

numeros = []

for numero in archivo.readlines():
    numeros.append(int(numero))

archivo.close()
print (sum(numeros))