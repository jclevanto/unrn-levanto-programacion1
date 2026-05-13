numeros = (4, 7, 2, 9, 7)

print(f"El primer numero es: {numeros[0]}")
print(f"El ultimo numero es: {numeros[-1]}")

contador=0
for i in numeros:
    if i == 7:
        contador +=1

print(f"El numero 7 aparece {contador} veces")

print(f"El largo de la tupla es {len(numeros)}")