flotante = input("Ingrese su numero flotante con un punto: ")

posi = -1
todo_ok = True

for indice, i in enumerate(flotante):
    if i == ".":
        if posi != -1:
            todo_ok = False
            break
        posi = indice

if posi != -1 and flotante[:posi].isnumeric() and flotante[posi+1:].isnumeric() and todo_ok:
    print("ok")
else:
    print("Hacelo bien loco")