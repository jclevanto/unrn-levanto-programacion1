archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/productos.csv","r")

productos={}

for producto in archivo.readlines()[1:]:
    nombre, precio, stock = producto.strip().split("; ")
    productos[nombre]={
        "precio":precio,
        "stock":stock
    }
archivo.close()

print(productos)