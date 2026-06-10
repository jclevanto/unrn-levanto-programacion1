cuadrados = []

for x in range (5):
    cuadrados .append(x**2)

print(cuadrados)

cuadrados = [x ** 2 for x in range (5)]
print(cuadrados)

lista=(1,2,3,4,5)

cuadrados_lista={x:x**2 for x in lista}
print(cuadrados_lista) 