mediciones = [
    ("temp", 18.5, "Aula 1"),
    ("humedad", 40, "Aula 1"),
    ("temp", 21.0, "Laboratorio"),
    ("presion", 1012, "Laboratorio"),
    ("humedad", 55, "Aula 2")
]

datos = {}
tipo_medicion=set()

for tipo, valor, lugar in mediciones:
    if not lugar in datos:
        datos[lugar]=[]
    datos[lugar].append(tipo + ": "+ str(valor))
    tipo_medicion.add(tipo)

print(datos)
print(tipo_medicion)