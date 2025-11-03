from tablaJuego import TablaJuego

class Usuario:
    def ingresarPosicion(self):
        tablajuego = TablaJuego()
        numeroUsuario=int(input("Ingresa una posicion : "))
        tablajuego.movimiento(numero=numeroUsuario, simbolo='0')
