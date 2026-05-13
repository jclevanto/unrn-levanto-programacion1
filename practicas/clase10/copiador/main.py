ruta = "practicas/clase10/copiador"

entrada = open(ruta + "/entrada/frase.txt","r")
salida = open(ruta + "/salida/frase_copia.txt","w")

salida.writelines(entrada)
entrada.close()
salida.close()