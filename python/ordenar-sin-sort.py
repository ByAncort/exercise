
num=[1,123,123,290,22,41,52,6,2131,213,9,99999999]
ordenada=[]
for i in num:
    contador=0
    for j in ordenada:
        # print(j)
        if i > j:
            contador +=1
        # print(contador,i)
        # print(contador)
    # print("insertamos  posicion=",contador,"valor",i)
    ordenada.insert(contador,i)
            
print(ordenada)

