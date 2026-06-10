cuadrados_pares = [x ** 2 for x in range (5) if (x ** 2)%2==0]
print(cuadrados_pares)

notas = [3,4,5,2,8,7]

estados=["Aprobado" if n>=6 else "Desaprobado" for n in notas]

print(estados)