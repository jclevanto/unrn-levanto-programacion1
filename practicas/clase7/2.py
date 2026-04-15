nums = [1,100,300,1000]

suma = 0
for i in nums:
    suma += i

canti = len(nums)
print(f"La suma de todos es {suma}")
print(f"Hay {canti} numeros")
print(f"El promedio es {suma//canti}")