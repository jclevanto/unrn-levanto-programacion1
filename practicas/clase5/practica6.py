def es_mayor(edad):
    if edad>=18:
        return True
    else:
        return False
    
if es_mayor(int(input("Ingrese la edad: "))):
    print("Es mayor")
else:
    print("Es menor maty")