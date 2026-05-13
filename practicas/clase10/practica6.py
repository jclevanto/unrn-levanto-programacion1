archivo = open("/workspaces/unrn-levanto-programacion1/practicas/clase10/personas.csv","r")
personas=[]

for persona in archivo.readlines()[1:]:
    nombre, apellido = persona.strip().split(",")
    personas.append({
        "nombre":nombre,
        "apellido":apellido
    })
archivo.close()

print(personas)