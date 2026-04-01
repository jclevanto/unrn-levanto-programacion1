salir = True
i=0
while salir:
    print(f"Estoy al principio de la iteracion {i}")
    i+=1
    if input("Ir a la proxima iteracion [si/no]: ") == "si":
        continue

    if input("Desea salir? [si/no]: ") == "si":
        salir=False
    print(f"Estoy al final de la iteracion {i-1}")
