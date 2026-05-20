def invertir_palabras(texto):
    resultado=""
    for i in range(len(texto)-1, -1, -1):
        if texto[i] == " ":
            resultado+=texto[i+1:] + " "
            texto = texto[:i]
    resultado += texto
    print(resultado)

invertir_palabras("hola mundo python")