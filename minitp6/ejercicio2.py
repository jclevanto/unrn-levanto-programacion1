inventario = {
    "cuaderno": {"precio": 2500, "stock": 4},
    "lapiz": {"precio": 800, "stock": 15},
    "goma": {"precio": 600, "stock": 2}
}

# Mostrar productos con stock bajo (stock < 5).
# Calcular valor total del inventario (precio * stock por producto).
# Generar un set con productos que requieren reposición urgente (stock <= 2).

inversion=0
urgente = set()

for i in inventario.keys():
    if inventario[i]["stock"]<5:
        print(f"El {i} necesita reponer stock")
    if inventario[i]["stock"]<=2:
        urgente.add(i)
    inversion+=inventario[i]["precio"] * inventario[i]["stock"]