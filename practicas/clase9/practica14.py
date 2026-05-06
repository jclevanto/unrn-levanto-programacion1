alumnos = [
    {
        "nombre" : "Joaquin",
        "notas" : [8, 7, 5],
        "materias" : {"Programacion", "Matematica"}
    },
    {
        "nombre" : "Juan",
        "notas" : [1, 1, 3],
        "materias" : {"Programacion"}
    },
    {
        "nombre" : "Lucia",
        "notas" : [8, 7, 1],
        "materias" : {"Programacion", "Ingles"}
    }
]
print("Nombres:")
for alumno in alumnos:
    print(alumno["nombre"])

for alumno in alumnos:
    total=0
    for nota in alumno["notas"]:
        total+=nota
    promedio = total/len(alumno["notas"])
    if promedio >=4:
        print(f"{alumno['nombre']} aprueba, saco {promedio:.2f}")
    else:
        print(f"{alumno['nombre']} no aprueba, saco {promedio:.2f}")

for alumno in alumnos:
    if "Matematica" in alumno ["materias"]:
        print(f"{alumno["nombre"]} cursa matematica")

alumnos[0]["materias"].add("Laboratorio")
print (alumnos[0])