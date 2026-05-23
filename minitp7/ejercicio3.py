nombres = [" mara ", "TOMAS", "  luCIA", "mARcos  ", " SOFIA "]
nombres_normalizados = []
for i in range(len(nombres)):
    nombres_normalizados.append(nombres[i].strip().capitalize())
print(nombres_normalizados)