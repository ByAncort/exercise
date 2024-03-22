numero=int(input("ingrese un numero entero positivo:  "))

factorial=1

for i in range(1,numero+1):
    factorial *= i

print("el factorial de ",numero,"es: ",factorial)