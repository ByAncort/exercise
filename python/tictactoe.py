from random import randrange
from os import system

def crear_tablero():
    return [['1', '2', '3'], ['4', 'X', '6'], ['7', '8', '9']]

def mostrar(tablero):
    print('-'*9)
    for fila in tablero:
        print(" | ".join(fila))       
        print('-'*9)

def user(n, tablero):
    if n in range(1, 10):
        fila = (n - 1) // 3
        columna = (n - 1) % 3
        if tablero[fila][columna] not in ['X', 'O']:
            tablero[fila][columna] = 'O'
            return True 
        else:
            print("La casilla seleccionada ya está ocupada. Intenta de nuevo.")
            return False  
    else:
        print("Movimiento inválido. Debes ingresar un número del 1 al 9.")
        return False  

def boot(tablero):
    while True:
        fila = randrange(3)
        columna = randrange(3)
        if tablero[fila][columna] not in ['X', 'O']:
            tablero[fila][columna] = 'X'
            break

def verificar_ganador(tablero):
    # Verifica filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2]:
            return fila[0]
    # Verifica columnas
    for i in range(3):
        if tablero[0][i] == tablero[1][i] == tablero[2][i]:
            return tablero[0][i]
    # Verifica diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] or tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[1][1]
    return None

def juego():
    tablero = crear_tablero()
    mostrar(tablero)

    while True:
        movimiento_valido = False
        while not movimiento_valido:
            try:
                n = int(input('Ingresa tu movimiento: '))
                movimiento_valido = user(n, tablero)
            except ValueError:
                print("Debes ingresar un número del 1 al 9.")
        mostrar(tablero)
        
        ganador = verificar_ganador(tablero)
        if ganador:
            print(f"¡{ganador} ha ganado!")
            break
        system("cls")
        boot(tablero)
        mostrar(tablero)
        
        ganador = verificar_ganador(tablero)
        if ganador:
            print(f"¡{ganador} ha ganado!")
            break


        
system("cls")
juego()
