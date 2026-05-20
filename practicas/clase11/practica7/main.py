numero = input("Ingrese la nota del parcial: ")

if numero.isnumeric():
    if 0<=int(numero)<=10:
        print(f"La nota {numero} es valida")
    else:
        print("No")
else:
    print("No")