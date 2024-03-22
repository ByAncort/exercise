def validador(pas):
    count_uppercase = sum(1 for char in pas if char.isupper())
    count_lowercase = sum(1 for char in pas if char.islower())
    count_special = sum(1 for i in pas if not i.isalnum() and i != ' ')

    if len(pas) < 10:
        print("La contraseña es muy corta.")
        print("Longitud           | {:<8}".format(len(pas)))
    elif count_uppercase < 1:
        print("Tiene pocas mayúsculas.")
        print("Mayúsculas         | {:<8}".format(count_uppercase))
    elif count_special < 2:
        print("Tiene pocos caracteres especiales.")
        print("Especiales         | {:<8}".format(count_special))
    else :
        print("Tipo de Carácter   | Cantidad")
        print("-------------------|---------")
        print("Mayúsculas         | {:<8}".format(count_uppercase))
        print("Minúsculas         | {:<8}".format(count_lowercase))
        print("Especiales         | {:<8}".format(count_special))
        print("Longitud Final     | {:<8}".format(len(pas)))
        print("-------------------|---------")
        print("Contraseña perfecta")
        

pas = input("Ingrese contraseña para ver su seguridad: ")
validador(pas)


