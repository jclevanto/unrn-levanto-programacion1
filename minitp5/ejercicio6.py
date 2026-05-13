producto = {"nombre": "Mouse", "precio": 12500, "stock": 6}

for i in producto.keys():
    print(i)

for i in producto.values():
    print(i)

for i in producto.keys():
    print(f"{i}: {producto[i]}")