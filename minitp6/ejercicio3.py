libros = [
    ("El Principito", "Antoine de Saint-Exupéry", 1943, "Novela"),
    ("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela"),
    ("Breves respuestas a las grandes preguntas", "Stephen Hawking", 2018, "Ciencia"),
    ("Sapiens", "Yuval Noah Harari", 2011, "Historia"),
    ("Física para la ciencia y la tecnología", "Serway", 2010, "Ciencia")
]

# Mostrar todos los títulos publicados después de 2010.
# Obtener un set con los géneros disponibles.
# Crear un diccionario donde la clave sea el género y el valor la cantidad de libros de ese género.
# Mostrar qué género tiene más libros.
# Mostrar los géneros sin repetirse.

print("Titulos publicados despues de 2010:")
for i in libros:
    if i[2]>2010:
        print(i[0])

generos={}
for i in libros:
    generos[i[3]]=0

cantidad={}
for i in generos:
    cantidad[i]=0

for i in libros:
    generos[i[3]]+=1

mayor=0
print(generos)
for i in generos.values():
    if i>mayor:
        mayor=i

print("Los generos con mayor cantidad de titulos:")
for i in generos.keys():
    if generos[i]==mayor:
        print(i)