libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("1984", "George Orwell", 1949, "Novela"),
    ("Rayuela", "Julio Cortázar", 1963, "Novela"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Armas, gérmenes y acero", "Jared Diamond", 1997, "Historia"),
    ("Historia mínima de América Latina", "Carlos Malamud", 2014, "Historia"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Cosmos", "Carl Sagan", 1980, "Ciencia"),
    ("Una breve historia del tiempo", "Stephen Hawking", 1988, "Ciencia"),
    ("El arte de la guerra", "Sun Tzu", -500, "Estrategia"),
    ("Pensar rápido, pensar despacio", "Daniel Kahneman", 2011, "Psicología")
]

print("Los generos disponibles son:")
generos = set()
for i in libros:
    generos.add(i[3])
for i in generos:
    print(i)

while(True):
    genero=input("Que genero desea buscar? ")
    if genero=="salir":
        break

    print("Los libros disponibles de ese genero son:")
    encontro=False
    for i in libros:
        if i[3]==genero:
            encontro=True
            print(i[0])
    
    if not encontro:
        print("No hay libros de ese genero")
