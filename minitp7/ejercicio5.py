codigo = input("Ingrese el codigo de la materia: ")
codigo=codigo.strip()

if codigo.count("-") == 1:
    letras,numeros=codigo.split("-")
    if letras.isalpha():
        if numeros.isnumeric():
            print("Codigo valido: ",codigo.upper())
        else:
            print("Los ultimos caracteres deben ser numeros PROG-101")
    else:
        print("Los primeros caracteres deben ser letras PROG-101")
else:
    print("Utilize un - para separar las letras y los numeros PROG-101")
