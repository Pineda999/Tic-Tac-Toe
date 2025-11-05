class TablaJuego:
    def __init__(self):
        # Tablero inicial 3x3 con valores del 1 al 9
        self.tablero = [[int(i) for i in range(1 + j * 3, 4 + j * 3)] for j in range(3)]
    

    def movimiento(self, numero=None, simbolo=None):
        for fila in range(3):
            for columna in range(3):
                if self.tablero[fila][columna] == numero:
                    self.tablero[fila][columna] = simbolo
        return self.tablero
    
    def obtener_tablero(self):
        return self.tablero

    def posiciones_libres(self):
        libres = []
        for i in range(3):
            for j in range(3):
                # 🔹 Si la casilla no está ocupada (ni 'X' ni 'O'), se considera libre
                if self.tablero[i][j] != 'X' and self.tablero[i][j] != 'O':
                    libres.append(i * 3 + j + 1)
        return libres
    
    def verificar_ganador(self):
        board = self.tablero
        # Filas
        for fila in board:
            if fila[0] == fila[1] == fila[2]:
                return fila[0]
        # Columnas
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        # Diagonales
        if board[0][0] == board[1][1] == board[2][2]:
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[0][2]
        
        # Empate → no hay ganador y no hay espacios libres
        if not self.posiciones_libres():
            return "Empate"
        
        return None  # nadie ha ganado todavía

