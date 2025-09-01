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
        jugador1 = jugador1.lower()
        jugador2 = jugador2.lower()

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

        for fila in tablero:
            if " " in fila:
                return "continua"

        return "empate"

    def generar_combinacion_mastermind(self, longitud, colores):
        return [random.choice(colores) for _ in range(longitud)]

    def validar_movimiento_torre_ajedrez(self, x1, y1, x2, y2, tablero):
        if x1 == x2 and y1 == y2:
            return False

        if x1 != x2 and y1 != y2:
            return False

        if x1 == x2:  
            paso = 1 if y2 > y1 else -1
            for y in range(y1 + paso, y2, paso):
                if tablero[x1][y] != " ":
                    return False

        elif y1 == y2: 
            paso = 1 if x2 > x1 else -1
            for x in range(x1 + paso, x2, paso):
                if tablero[x][y1] != " ":
                    return False

        return True