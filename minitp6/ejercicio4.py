estudiantes = [
    {"nombre": "Ana", "notas": [7, 8, 6], "asistencias": 9, "comision": "C1"},
    {"nombre": "Luis", "notas": [4, 5, 3], "asistencias": 6, "comision": "C1"},
    {"nombre": "Mora", "notas": [9, 8, 10], "asistencias": 10, "comision": "C2"},
    {"nombre": "Pedro", "notas": [2, 4, 3], "asistencias": 7, "comision": "C2"}
]


    # Promociona si promedio >= 8 y asistencias >= 8
    # Regulariza si promedio >= 4 y asistencias >= 6
    # Recursa en otro caso

    # Mostrar cuántos estudiantes hay en cada categoría.
    # Mostrar la comisión con mejor promedio general.
    # Generar un set con nombres de estudiantes en riesgo (Recursa).

for i in estudiantes:
    i["promedio"]=sum(i["notas"])/len(i["notas"])

promociona=0
regulariza=0
recursa=0
for i in estudiantes:
    if i["promedio"]>=8 and i["asistencias"]>=8:
        promociona+=1
    elif i["promedio"]>=4 and i["asistencias"]>=6:
        regulariza+=1
    else:
        recursa+=1

print(f"Promociona {promociona} estudiantes")
print(f"Regularizan {regulariza} estudiantes")
print(f"Recursa {recursa} estudiantes")

mejor={}
for i in estudiantes:
    mejor[i["comision"]]=[]

for i in estudiantes:
    mejor[i["comision"]].append(i["promedio"])

# print(mejor)
el_mejor=0
for i in mejor.keys():
    if sum(mejor[i])/len(mejor[i]):
        el_mejor=i
print(f"La mejor comision es la {el_mejor}")