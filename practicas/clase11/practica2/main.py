usuarios = [
    "ana,programacion",
    "juan,matematica",
    "lucia,fisica"
]

for usuario in usuarios:
    nombre=usuario.split(",")
    print(f"Hola {nombre[0].capitalize()}, estas inscripto/a en {nombre[1].capitalize()}.")