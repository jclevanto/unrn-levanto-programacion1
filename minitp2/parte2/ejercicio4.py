#temperatura=15
temperatura=int(input("Que temperatura hace? "))

if (temperatura<10):
    print("Lleva abrigo")

elif(temperatura<20):
    print("Lleva ropa media")

else:
    print("Lleva ropa liviana")