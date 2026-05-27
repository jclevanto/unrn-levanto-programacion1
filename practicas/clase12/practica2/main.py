puertas=[
"PUERTA_A;ABIERTA;18:03",
"PUERTA_B;CERRADA;18:04",
"PUERTA_A;ABIERTA;18:05"
]

cantidad={}
for dato in puertas:
    cantidad[dato.split(";")[0]]=0
for dato in puertas:
    cantidad[dato.split(";")[0]]+=1

print(cantidad)

datos= [3.2, 3.4, 5.1, 2.9, 6.0, 3.3]
contador=0

for i in datos:
    if i<3.0 or i>5.0:
        contador+=1
print(contador)

instrucciones_validas=["encender","apagar","estado"]
while(True):
    instruccion=input("Ingrese su instruccion: ")
    instruccion=instruccion.lower().strip()
    if instruccion in instrucciones_validas:
        print("Instruccion valida")
    else:
        print("instruccion invalida")
