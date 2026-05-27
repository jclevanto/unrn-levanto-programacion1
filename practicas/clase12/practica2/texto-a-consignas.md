Crearia un diccionario, donde la key sea el nombre de la puerta
y por cada vez que aparezca la puerta sumaria 1 al valor, haciendo un split a los valores para separar la puerta del resto, recorriendo antes por primera vez la lista definiendo cuales puertas hay y definiendo su cantidad en 0:

```python
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
```

Recorreria la lista y sumaria 1 a un contador en caso de que el valor sea menor que 3.0 o mayor que 5.0:

```python
datos= [3.2, 3.4, 5.1, 2.9, 6.0, 3.3]
contador=0

for i in datos:
    if i<3.0 or i>5.0:
        contador+=1
print(contador)
```

Le pediria al usuario la instruccion, le haria un lower y un strip y comprobaria si esta en una lista de instrucciones validas:

```python
instrucciones_validas=["encender","apagar","estado"]
while(True):
    instruccion=input("Ingrese su instruccion: ")
    instruccion=instruccion.lower().strip()
    if instruccion in instrucciones_validas:
        print("Instruccion valida")
    else:
        print("instruccion invalida")
```