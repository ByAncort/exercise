#divir numeros impares sin desimal y sin restante

def dividir_numero(numero): 
    parte1 = numero // 2
    if numero % 2 != 0:
        parte1 = parte1 + 1
    parte2 = numero - parte1
    return parte1, parte2


numero_inicial = int(input("Ingrese un número: "))
parte_1, parte_2 = dividir_numero(numero_inicial)
print("Primera parte:", parte_1)
print("Segunda parte:", parte_2)
