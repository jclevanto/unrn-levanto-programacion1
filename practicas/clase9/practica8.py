nombres = ["Ana","Juan","Ana","Pedro","Juan","Lucia"]
nombres_unicos = set (nombres)

print("Los nombres unicos son:")
for i in nombres_unicos:
    print(i)

print(f"Hay {len(nombres_unicos)} nombres")