alumnos = [
    {"Nombre":"Paula","Nota":8},
    {"Nombre":"Juan","Nota":3},
    {"Nombre":"Pedro","Nota":6},
]

alumnos.append(
    {"Nombre":"Jhon","Nota":2},
)

for alumno in alumnos:
    if alumno["Nota"] >= 4:
        print(alumno["Nombre"], "aprobo")
    else:
        print(alumno["Nombre"], "desaprobo")