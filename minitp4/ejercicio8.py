def pedir_comida():
    comida=input("Que quiere comer?: ")
    while True:
        if comida == "pizza" or comida == "milanesa" or comida == "hamburguesa":
            return comida
        else:
            comida=input("Comida invalida pruebe otra cosa: ")

def obtener_precio(comida):
    if comida == "pizza":
        print("La pizza sale $140")
        return 140
    
    elif comida == "milanesa":
        print("La milanesa sale $125")
        return 125
    
    else:
        print("La hamburguesa sale $100")
        return 100
    
comida=pedir_comida()
obtener_precio(comida)