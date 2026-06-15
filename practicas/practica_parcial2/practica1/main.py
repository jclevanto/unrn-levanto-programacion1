eventos = [
    ("zona_a", "movimiento"),
    ("zona_b", "puerta"),
    ("zona_a", "puerta"),
    ("zona_c", "movimiento"),
    ("zona_b", "movimiento"),
    ("zona_a", "movimiento")
]

# Armar un diccionario donde la clave sea la zona y el valor sea la cantidad de eventos registrados en esa zona.
# Armar un conjunto con los tipos de eventos que aparecieron.
# Mostrar el diccionario final.
# Mostrar el conjunto final.

cantidades={}
tipo_de_evento=set()

for zona, evento in eventos:
    if not zona in cantidades:
        cantidades[zona]=0
    cantidades[zona]+=1
    tipo_de_evento.add(evento)

print(cantidades)
print(tipo_de_evento)