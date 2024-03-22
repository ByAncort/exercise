oracion=str(input("ingrese una oracion:  "))

total=0

for j in oracion:
    if j.lower() == 'a':
        total += 1  
    elif j.lower() == 'e':
        total += 1  
    elif j.lower() == 'i':
        total += 1  
    elif j.lower() == 'o':
        total += 1  
    elif j.lower() == 'u':
        total += 1  
    
if total!=0:
    print('La oracion tiene:  ',total ,'Vocales')
else:
    print('no tiene ninguna vocal')
