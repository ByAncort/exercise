class Personaje:
    def __init__(self, nombre, fuerza, iq, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.iq = iq
        self.defensa = defensa
        self.vida = vida

    def attribute(self):
        print(self.nombre, ":", sep="")
        print("fuerza", self.fuerza)
        print("inteligencia:", self.iq)
        print("defensa:", self.defensa)
        print("vida:", self.vida)

    def subir_nivel(self, fuerzaplus, iqplus, defensaplus, vidaplus):
        self.fuerza += fuerzaplus
        self.iq += iqplus
        self.defensa += defensaplus
        self.vida += vidaplus
    
    def esta_vivo(self):
        return self.vida > 0
    
    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = max(0, enemigo.vida - daño)  # Asegura que la vida no sea negativa
        print(self.nombre, "ha realizado", daño, "puntos de daño a", enemigo.nombre)
        if enemigo.esta_vivo():
            print("Vida de", enemigo.nombre, "es", enemigo.vida)
        else:
            enemigo.muerte()

    def muerte(self):
        print(self.nombre, "ha muerto.")


class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, iq, defensa, vida, arma):
        super().__init__(nombre, fuerza, iq, defensa, vida)
        self.arma = arma
    
    def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10.\n"))
        if opcion == 1:
            self.arma = 8
        elif opcion == 2:
            self.arma = 10
        else:
            print("\nNúmero de arma incorrecto") 
     
    def attribute(self):
        super().attribute()
        print("espada:", self.arma)
     
    def daño(self, enemigo):
        return max(0, self.fuerza - enemigo.defensa) * self.arma  # Asegura que el daño no sea negativo


class Mago(Personaje):
    def __init__(self, nombre, fuerza, iq, defensa, vida, varita):
        super().__init__(nombre, fuerza, iq, defensa, vida)
        self.varita = varita
    
    def cambiar_varita(self):
        opcion = int(input("Elige una varita: (1) Varita de Fuego, daño 12. (2) Varita de Hielo, daño 10.\n"))
        if opcion == 1:
            self.varita = 12
        elif opcion == 2:
            self.varita = 10
        else:
            print("\nNúmero de varita incorrecto") 
    
    def attribute(self):
        super().attribute()
        print("varita:", self.varita)

    def daño(self, enemigo):
        return max(0, self.iq * self.varita - enemigo.defensa)  # Asegura que el daño no sea negativo


def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre, ":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre, ":", sep="")
        jugador_2.atacar(jugador_1)
        turno += 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")


# Ejemplo de uso
personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

personaje_1.attribute()
personaje_2.attribute()      

combate(personaje_1, personaje_2)
