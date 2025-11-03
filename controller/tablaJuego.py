class TablaJuego:

    def mostrarTablero (self):
        tablero= [[int(i) for i in range(1+j*3, 4+j*3)] for j in range(3)]
        return tablero
    
    def movimiento(self, numero = None, simbolo = None):
        board=self.mostrarTablero()
        for fila in range(3):
            for columna in range(len(board)):
                if board[fila][columna]== numero:
                    board[fila][columna]=simbolo
            
        return board