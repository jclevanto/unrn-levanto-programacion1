patente = input("Ingrese la patente con el formato AB123CD: ")

if patente.isalnum() and len(patente)==7 and patente[:1].isalpha() and patente[2:4].isnumeric() and patente[4:]:
    print("todo ok")
else:
    print("okn't")
