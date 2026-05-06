producto = {
    "Nombre" : "Papas fritas",
    "Valor" : 150,
    "Stock" : 124
}

print(f"Las {producto['Nombre']} salen {producto['Valor']} y quedan {producto['Stock']}")

producto["Valor"] = int(producto["Valor"] * 1.1)

producto["Stock"] -= 1

print(f"Producto: {producto['Nombre']} - Precio actualizado: {producto['Valor']} - Stock restante: {producto['Stock']}")
