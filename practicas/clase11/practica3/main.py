def camello(texto):
    lista=texto.split()
    final=""
    final+=lista[0]
    for palabra in lista[1:]:
        final+=" " + palabra.capitalize()
    print(final)
    return final

camello("pedro MARTINEZ sEgundo")