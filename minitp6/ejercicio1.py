registros = [
    ("2026-04-07", "Bariloche", 18),
    ("2026-04-07", "Viedma", 31),
    ("2026-04-07", "El Bolson", 24),
    ("2026-04-14", "Bariloche", 20),
    ("2026-04-14", "Viedma", 29),
    ("2026-04-14", "El Bolson", 22),
    ("2026-04-21", "Bariloche", 17),
    ("2026-04-21", "Viedma", 27),
    ("2026-04-21", "El Bolson", 19)
]

# Mostrar todas las ciudades sin repetir (usar set).
# Mostrar todas las fechas disponibles sin repetir.
# Calcular el promedio de temperatura por ciudad (usar diccionario).
# Indicar qué ciudad tuvo el mayor promedio.

ciudades = set()
fechas = set()

for i in registros:
    ciudades.add(i[1])
    fechas.add(i[0])

print(ciudades)
print(fechas)

temperaturas={}
for i in ciudades:
    temperaturas[i]=0

for i in registros:
    temperaturas[i[1]]+=i[2]
print(temperaturas)

canti_ciudades={}
for i in ciudades:
    contador=0
    for j in registros:
        if i == j[1]:
            contador+=1
    canti_ciudades[i]=contador

for i in ciudades:
    print(f"La temperatura promedio en {i} fue {temperaturas[i]/canti_ciudades[i]:.2f}")