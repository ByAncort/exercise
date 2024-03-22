n = []
n.append(float(input("Ingrese cantidad a invertir: ")))
n.append(float(input("Ingrese interés anual: ")))
n.append(int(input("Ingrese numero de años: ")))

for i in range(1, n[2] +1):
    capital_obtenido = n[0] + (n[0] * (n[1] / 100))
    print(i, "año. Capital obtenido:", capital_obtenido)
    n[0] = capital_obtenido


print(n)
