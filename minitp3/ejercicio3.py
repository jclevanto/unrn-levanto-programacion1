lista = []
mensaje=""

while (mensaje != "fin"):
    mensaje=input("Ingrese su numero, salga escribiendo fin: ")
    lista.append(mensaje)

lista.remove("fin")

print(lista)

print(f"La lista tiene {len(lista)} elementos")