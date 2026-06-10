import os

tablero=[[" - "," - "," - "],[" - "," - "," - "],[" - "," - "," - "]]

def imprimir_tablero(valores):
    for i in range (3):
        #print("   |   |   ")
        print(f" {valores[i][0]} | {valores[i][1]} | {valores[i][2]} ")
        #print("   |   |   ")
        if i != 2:
            print("-----------------")
#print(tablero)

def comprobar_ganador(tablero):
    for i in range (3):
        if tablero[i][0]==tablero[i][1]==tablero[i][2]:
            if tablero[i][0] != " - ":
                return True
        if tablero[0][i]==tablero[1][i]==tablero[2][i]:
            if tablero[0][i] != " - ":
                return True
    if tablero[0][0]==tablero[1][1]==tablero[2][2]:
        if tablero[0][0] != " - ":
            return True
    if tablero[0][2]==tablero[1][1]==tablero[2][0]:
        if tablero[2][0] != " - ":
            return True
    return False
iteracion=0
while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    imprimir_tablero(tablero)
    while (True):
        if iteracion%2==0:
            print("Turno de ⭕")
            turno="⭕ "
        else:
            print("Turno de ❌")
            turno ="❌ "
        coordenada=input("Ingrese la coordenada que quiere usar x,y ")
        coordenada=coordenada.strip()
        #print(coordenada)
        if not (len(coordenada)==3 and "," in coordenada):
            print("Formato incorrecto")
            break
        else:
            y,x=coordenada.split(",")
            if not (x.isnumeric() and y.isnumeric()):
                print("Formato incorrecto")
                break
            else:
                x=int(x)-1
                y=int(y)-1
                if not (0 <= x <= 2 and 0 <= y <= 2):
                    print("Posicion fuera de rango")
                    break
                if tablero[x][y] != " - ":
                    print("Posicion ocupada")
                    break
                tablero[x][y]=turno
                iteracion+=1
                break
    if comprobar_ganador(tablero):
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_tablero(tablero)
        print(f"{turno} gano")
        break
    if iteracion==9:
        os.system('cls' if os.name == 'nt' else 'clear')
        imprimir_tablero(tablero)
        print("Empate")
        break
