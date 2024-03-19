import math

def calcular_cuadrante(x, y):
    if x > 0 and y > 0:
        return "primer cuadrante"
    elif x < 0 and y > 0:
        return "segundo cuadrante"
    elif x < 0 and y < 0:
        return "tercer cuadrante"
    elif x > 0 and y < 0:
        return "cuarto cuadrante"
    elif x == 0 and y != 0:
        return "sobre el eje Y"
    elif y == 0 and x != 0:
        return "sobre el eje X"
    else:
        return "origen"

def calcular_area_perimetro(x, y):
    cuadrante = calcular_cuadrante(x, y)
    if cuadrante != "origen":
        if cuadrante != "sobre el eje X" and cuadrante != "sobre el eje Y":
            area = 0.5 * abs(x) * abs(y)
            perimetro = abs(x) + abs(y) + math.sqrt(x**2 + y**2)
            return area, perimetro
        else:
            if cuadrante == "sobre el eje X":
                area = abs(y)
                perimetro = 2 * abs(y) + 2
                return area, perimetro
            else:  # Sobre el eje Y
                area = abs(x)
                perimetro = 2 * abs(x) + 2
                return area, perimetro
    else:
        return None, None

def main():
    x = float(input("Ingrese la coordenada x: "))
    y = float(input("Ingrese la coordenada y: "))

    cuadrante = calcular_cuadrante(x, y)
    print(f"El punto ({x}, {y}) está en el {cuadrante}.")

    area, perimetro = calcular_area_perimetro(x, y)
    if area is not None:
        print(f"El área de la figura es: {area}")
        print(f"El perímetro de la figura es: {perimetro}")
    else:
        print("No se forma una figura geométrica con área o perímetro.")

if __name__ == "__main__":
    main()
