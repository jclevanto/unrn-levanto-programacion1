usuario = {
    "Usuario" : "Juan",
    "Mail" : "jclevanto@gmail.com",
    "Activo" : True
}
# nuevo = {
#     "Usuario" : "Juan",
#     "Mail" : "jclevanto@gmail.com",
#     "Activo" : True
# }
nuevo = usuario

print(f"El mail es {nuevo['Mail']}")
nuevo["Activo"] = False
nuevo["Ultimo_login"] = "6/5/2026"

for i, j in nuevo.items():
    print(f"{i}: {j}")
