lista = []
mensaje=""

while ((mensaje != "fin") and (len(lista)<5)):
    mensaje=input("Ingrese su numero, salga escribiendo fin: ")
    lista.append(mensaje) 

if lista[-1]=="fin":
    lista.remove("fin")

print(lista)

print(f"La lista tiene {len(lista)} elementos")