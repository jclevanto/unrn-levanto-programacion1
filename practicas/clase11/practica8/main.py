productos = input("Ingrese sus productos separados por comas: ")

if productos.count(",")>=1:
    lista=productos.split(",")
    for i in lista:
        if i == "" or i == " ":
            print("Ingreso un producto vacio")
            break
else:
    print("Ingrese al menos 2 productos")