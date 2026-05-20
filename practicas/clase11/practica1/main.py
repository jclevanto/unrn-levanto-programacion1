lineas=[
    " Ana ;8;7;9",
    " JuAn ;4;5;3",
    " LucIA ;10;9;10"
]

for linea in lineas:
    texto=linea.split(";")
    texto[0] = texto[0].strip().capitalize()
    print(f"Alumno '{texto[0]}' - Notas: {" - ".join(texto[1:])}")