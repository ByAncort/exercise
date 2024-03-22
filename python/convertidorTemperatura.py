def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def main():
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    opcion_entrada = int(input("Selecciona la opción de entrada (1/2/3): "))
    valor_entrada = float(input("Ingresa el valor a convertir: "))

    print("\nSelecciona la opción de salida (1/2/3): ")
    opcion_salida = int(input("1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))

    if opcion_entrada == 1:
        if opcion_salida == 1:
            resultado = valor_entrada
        elif opcion_salida == 2:
            resultado = celsius_to_fahrenheit(valor_entrada)
        elif opcion_salida == 3:
            resultado = celsius_to_kelvin(valor_entrada)
    elif opcion_entrada == 2:
        if opcion_salida == 1:
            resultado = fahrenheit_to_celsius(valor_entrada)
        elif opcion_salida == 2:
            resultado = valor_entrada
        elif opcion_salida == 3:
            resultado = fahrenheit_to_kelvin(valor_entrada)
    elif opcion_entrada == 3:
        if opcion_salida == 1:
            resultado = kelvin_to_celsius(valor_entrada)
        elif opcion_salida == 2:
            resultado = kelvin_to_fahrenheit(valor_entrada)
        elif opcion_salida == 3:
            resultado = valor_entrada

    print(f"El resultado de la conversión es: {resultado}")

if __name__ == "__main__":
    main()
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def fahrenheit_to_kelvin(fahrenheit):
    kelvin = (fahrenheit - 32) * 5/9 + 273.15
    return kelvin

def kelvin_to_fahrenheit(kelvin):
    fahrenheit = (kelvin - 273.15) * 9/5 + 32
    return fahrenheit

def main():
    print("1. Celsius")
    print("2. Fahrenheit")
    print("3. Kelvin")
    opcion_entrada = int(input("Selecciona la opción de entrada (1/2/3): "))
    valor_entrada = float(input("Ingresa el valor a convertir: "))

    print("\nSelecciona la opción de salida (1/2/3): ")
    opcion_salida = int(input("1. Celsius\n2. Fahrenheit\n3. Kelvin\n"))

    if opcion_entrada == 1:
        if opcion_salida == 1:
            resultado = valor_entrada
        elif opcion_salida == 2:
            resultado = celsius_to_fahrenheit(valor_entrada)
        elif opcion_salida == 3:
            resultado = celsius_to_kelvin(valor_entrada)
    elif opcion_entrada == 2:
        if opcion_salida == 1:
            resultado = fahrenheit_to_celsius(valor_entrada)
        elif opcion_salida == 2:
            resultado = valor_entrada
        elif opcion_salida == 3:
            resultado = fahrenheit_to_kelvin(valor_entrada)
    elif opcion_entrada == 3:
        if opcion_salida == 1:
            resultado = kelvin_to_celsius(valor_entrada)
        elif opcion_salida == 2:
            resultado = kelvin_to_fahrenheit(valor_entrada)
        elif opcion_salida == 3:
            resultado = valor_entrada

    print(f"El resultado de la conversión es: {resultado}")

if __name__ == "__main__":
    main()
