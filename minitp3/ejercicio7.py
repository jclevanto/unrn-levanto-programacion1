lista = []
pedido = ""

while pedido != "terminar":
    pedido = input("Desea pedir pizza, hamburguesa, empanada o terminar? ")

    if pedido not in ["pizza", "hamburguesa", "empanada", "terminar"]:
        print("La opcion seleccionada no esta en el menu")
    elif pedido != "terminar":
        print("Agregado")
        lista.append(pedido)

print("El pedido es: ")
for i in lista:
    print(i)

print(f"Y tiene {len(lista)} items")