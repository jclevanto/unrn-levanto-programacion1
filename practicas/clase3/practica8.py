nombres=["Juan","Pedro","Mateo"]
platos_persona = [0,0,0]
platos=int(input("Cuantos platos hay para lavar? "))
lavados=0

for i in range (platos):
    platos_persona[lavados]+=1
    print(f"{i+1}. {nombres[lavados]} lavo su plato n° {platos_persona[lavados]}")
    lavados+=1
    if (lavados==3):
        lavados=0