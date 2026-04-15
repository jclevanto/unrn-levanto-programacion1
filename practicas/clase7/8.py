cantidad = 0
numero = 2
total = 0

while (numero!=0):
    numero = int(input("Ingrese un numero o 0 para salir: "))
    total += numero
    cantidad += 1

print(f"La suma de todos los numeros es {total}")
print(f"Se ingresaron {cantidad-1} numeros")
print(f"El promedio fue {total/(cantidad-1)}")