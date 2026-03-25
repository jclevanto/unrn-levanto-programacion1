opcion = ""

print("Seleccione la comida para llevar")
while opcion != "terminar pedido":
    opcion = input("Escriba la comida que quieras agregar al pedido: ").lower()
    if opcion == "pizza":
        print("Excelente! Agregamos una pizza a tu pedido")
    elif opcion == "terminar pedido":
        print("Cerrando pedido")
    elif opcion == "hamburguesa":
        print("Excelente! Agregamos una hamburguesa a tu pedido")
    elif opcion == "helado":
        print("Excelente! Agregamos un helado a tu pedido")
    elif opcion == "carne":
        print("Excelente! Agregamos helado a tu pedido")
    else:
        print(f"Lo siento, no tenemos {opcion}, prueba con otra cosa")
print("Pedido finalizado, gracias por confiar en nosotros")