datosPersonales= ['null']

datosPersonales[0] =input("ingrese sus nombres:  ")
lastNameD =input("ingrese su apellido paterno:  ")
lastNameM =input("ingrese su apellido materno:  ")
datosPersonales.append(lastNameD)
datosPersonales.append(lastNameM)


for i in datosPersonales:
    print(i)
    for j in range(10):
        print(i)

#print(datosPersonales)


