import random

class numeroRandom:
    def __init__(self):
        self.lista_numero = []

    def numeroAleatorio(self):
        # Generar número entre 1 y 9 (coincide con tu tablero 3x3)
        return random.randint(1, 9)

    def verificarNumero(self, libres):
        if  not  libres:
            return 1
        numero = random.choice(libres)
        return numero
       