import random
def bucle_adi(num):
    opc=0
    while opc !=num:
        opc=int(input("intenta adivinar el numero del 1 al 10:  "))
        if opc > num:
            print("mas bajo")
        elif opc < num:
            print("mas alto")
        else:
            print("Ganaste Mmahuevo!!!")

num=random.randint(1, 6)
bucle_adi(num)






