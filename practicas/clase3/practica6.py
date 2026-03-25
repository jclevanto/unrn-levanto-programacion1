
dni=bool(input("Tenes DNI? [S/n]: ")=="S")
edad = int(input("Que edad tenes? "))

if (dni and edad>=18):
    print("Pase")
else :
    print("No pase")
