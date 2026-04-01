def trae_documento():
    return input("Trae documento [si/no]? ") == "si"

def ingresar_edad():
    return(int(input("Ingrese su edad: ")))

def puede_pasar(docuemtno, edad):
    return docuemtno == True and edad>=18

decomento=trae_documento()
edad=ingresar_edad()

if puede_pasar(decomento,edad):
    print("Puede pasar")

else:
    print("No puede pasar")