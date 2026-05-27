# # Interpretando consignas

# ## Verificaciones

# 1. Se pide verificar que un dato es un número?

# "5".isnumeric()

# 2. Se pide verificar que tiene N cantidad de caracteres?

# len("hola")==4

# 3. Se pide verificar que no sea un dato vacío?

# "hola" != ""

# 4. Se pide verificar que un elemento más exista más de N veces?

# "hola mundo".count("o")>1

# 5. Si tenemos que verificar que un texto contenga otro texto?

# "hola" in "hola mundo"

# ## Repeticiones

# 1. Tenemos una lista de 25 datos, hay que verificar que todos sean números. ¿Qué hacemos?

# lista = ["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25"]
# for i in lista:
#     if not i.isnumeric():
#         print("No papi")

# 2. Hay que pedirle 5 nombres al usuario. ¿Que hacemos?

# nombres=[]
# for i in range(5):
#     nombres.append(input("Nombre: "))

# # 3. Tenemos que pedir datos al usuario hasta que digan FIN. ¿Que usamos?

# while True:
#     dato=input("Ingrese el dato o fin para salir: ")
#     if dato.lower() == "fin":
#         break

# ## Archivos

# 1. Hay que leer un archivo: 

# ruta = "practicas/clase12/practica1/"
# archivo = open(ruta+"archivo.txt","r")
# print(archivo.read())

# 2. Hay que escribir un archivo:

# archivo = open(ruta+"archivo.txt","w")
# archivo.write("Que\nOnda\nAmigo")

# 3. ¿Hay que cerrar un archivo?

# archivo.close()

# ## Otros
# 1. Tenemos que solicitarle al usuario nombre, apellido y año de nacimiento ¿Que hacemos? 

# datos=input("Ingrese su nombre, apellido y edad separados por comas: ")
# lista=datos.split(",")
# if not (lista[0].strip().isalpha() and lista[1].strip().isalpha() and lista[2].strip().isnumeric()):
#     print("todo mal")

# 2. Si tenemos que crear una estructura que tiene el nombre de producto como clave, dentro tenemos que tener precio, stock y tipo de producto. Usar la estructura más semántica posible.

# estructura={
#     "pizza":{"precio":123,"stock":32,"tipo":"comida"}
# }

# print(estructura["pizza"]["precio"])
