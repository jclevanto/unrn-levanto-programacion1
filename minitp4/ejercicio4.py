def calcular_descuento(valor):
    if valor <= 1000:
        return valor

    return int(valor * 0.9)

total = int(input("Cual es el valor total de la compra?: "))
conde = calcular_descuento(total)

if conde == total:
    print(f"El precio final es {total}, no se aplico descuento")
else:
    print(f"El precio final es {conde}, se aplico un 10% de descuento")