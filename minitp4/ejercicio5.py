def obtener_estado(nota):
    if nota >= 8:
        return "Promociona"
    elif nota >= 6:
        return "Aprueba"
    
    return "Desaprueba :("

nota = int(input("Cual fue la nota?: "))
print(obtener_estado(nota))