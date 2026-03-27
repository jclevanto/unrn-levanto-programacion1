lista = ["pizza", "empanadas", "hamburguesa"]
encontro=False

busco=input("Que desea buscar en la lista? ")

for i in range (len(lista)):
    if lista[i]==busco:
        print(f"El elemento {busco} esta en la poscicion {i} de la lista")
        encontro=True
        i=len(lista)

if not encontro:
    print("El elemento no esta en la lista")