import random
from tablaJuego import TablaJuego

class numeroRandom:
    def __init__(self):
        self.lista_numero=[]
    
    def numeroAleatorio(self):
        numeroGenerado = random.randint(1,10)
        return numeroGenerado
    
    def verificarNumero(self):        
        numerogenerado = self.numeroAleatorio()

        if numerogenerado in self.lista_numero:
            return "Todos los numeros fueron sorteados"
        else:
            self.lista_numero.append(numerogenerado)
            return numerogenerado
