import random
import string



longitud=int(input("ingrese la longitud de la contraseña:  "))
caracter = string.ascii_letters + string.digits + string.punctuation
contrasena = ''.join(random.choice(caracter) for i in range((longitud)))
print(contrasena)