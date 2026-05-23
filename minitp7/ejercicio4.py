edad = input("Ingrese su edad: ")
edad=edad.strip()
bien = True
if edad.isnumeric():
    edad=int(edad)
else:
    print("Ingrese la edad numericamente")
    bien = False

if bien:
    if 0<edad<120:
        print(f"Edad registrada: {edad}")
    else:
        print("Ingrese una edad entro 0 y 120")

