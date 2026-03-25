numero=int(input("Ingrese el numero: "))

if (numero%2==0):
    print(f"El numero {numero} es par")
else:
    print(f"El numero {numero} es impar")

if (numero<10):
    print("El numero es menor a 10")
elif(numero==10):
    print("El numero es igual a 10")
else:
    print("El numero es mayor a 10")