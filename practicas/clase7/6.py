def mando_saludo():
    print("Hola amigo")

def envio_saludo():
    return ("Hola amigo")

def saludo_personalizado(nombre):
    return (f"Hola {nombre}")

mando_saludo()

print(envio_saludo())

print(saludo_personalizado("Juan"))