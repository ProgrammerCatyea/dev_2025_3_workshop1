import random

class Games:
    def adivinar_numero_pista(self, numero_secreto, intento):
        if intento == numero_secreto:
            return "correcto"
        elif intento > numero_secreto:
            return "muy alto"
        else:
            return "muy bajo"

    def piedra_papel_tijera(self, jugador1, jugador2):
      
        jugador1 = jugador1.lower().strip()
        jugador2 = jugador2.lower().strip()
        opciones = {"piedra", "papel", "tijera"}

        if jugador1 not in opciones or jugador2 not in opciones:
            return "invalid"

        if jugador1 == jugador2:
            return "empate"

        reglas = {
            "piedra": "tijera",
            "tijera": "papel",
            "papel": "piedra",
        }

        if reglas[jugador1] == jugador2:
            return "jugador1"
        else:
            return "jugador2"

    def ta_te_ti_ganador(self, tablero):
   
        for fila in tablero:
            if fila[0] == fila[1] == fila[2] and fila[0] != " ":
                return fila[0]

  
        for col in range(3):
            if tablero[0][col] == tablero[1][col] == tablero[2][col] and tablero[0][col] != " ":
                return tablero[0][col]

     
        if tablero[0][0] == tablero[1][1] == tablero[2][2] and tablero[0][0] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] and tablero[0][2] != " ":
            return tablero[0][2]

    
        return "continua"

    def generar_combinacion_mastermind(self, longitud, colores):
       
        return [random.choice(colores) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, desde_fila, desde_col, hasta_fila, hasta_col, tablero):
       
        filas = len(tablero)
        columnas = len(tablero[0]) if filas > 0 else 0
        if not (0 <= desde_fila < filas and 0 <= desde_col < columnas and
                0 <= hasta_fila < filas and 0 <= hasta_col < columnas):
            return False

        if desde_fila == hasta_fila and desde_col == hasta_col:
            return False

        if desde_fila != hasta_fila and desde_col != hasta_col:
            return False

        if desde_fila == hasta_fila:
            paso = 1 if hasta_col > desde_col else -1
            for c in range(desde_col + paso, hasta_col, paso):
                if tablero[desde_fila][c] != " ":
                    return False

       
        else:
            paso = 1 if hasta_fila > desde_fila else -1
            for r in range(desde_fila + paso, hasta_fila, paso):
                if tablero[r][desde_col] != " ":
                    return False

        return True