menu= ["pizza","hamburguesa","pollo"]
precio = [1,3,5]
total = 0
opcion = ""

print("Seleccione la comida para llevar")
print("Nuestro menu: ")
for i in menu:
    print(f"-{i}")
print("Termine su pedido con Terminar pedido")
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    for i in (menu):
        pidio=False
        if opcion == i:
            print(f"Excelente! Agregamos un/a {i} a tu pedido")
            posicion=0
            for a in menu:
                if a == i:
                    total+=precio[posicion]
                posicion+=1
            pidio=True
        elif opcion == "terminar pedido":
            print("Cerrando pedido")
            pidio=True
            break
    if not pidio:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")

if total!=0:
    print(f"Pedido finalizado, su total es {total}$, gracias por confiar en nosotros")
else:
    print("Gracias")