def es_par(numero):
    return not numero % 2

num = int(input("Ingrese el numero: "))
condicion = es_par (num)

if condicion:
    print(f"El numero {num} es par")

else:
    print(f"El numero {num} es impar")