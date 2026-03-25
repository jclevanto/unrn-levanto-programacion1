#edad = 20
#tiene_documento = True

edad=int(input("Ingrese su edad: "))
tiene_documento=bool((input("Trae documento? [S/n]: ")=="S"))

if (edad>=18 and tiene_documento):
    print("Podes pasar")
else :
    print("No podes pasar")