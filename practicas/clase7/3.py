x = [10, -1, 2, 3, 5, 7, 6, -7, 8, -10]

maximo = x[0]
minimo = x[0]

for i in x:
    if i < minimo:
        minimo = i
    
    if i > maximo:
        maximo = i

print(f"El numero mas grande es {maximo}")
print(f"El numero mas chico es {minimo}")