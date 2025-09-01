class Games:
    def piedra_papel_tijera(self, jug1, jug2):
        jug1, jug2 = jug1.lower(), jug2.lower()
        opciones = ["piedra", "papel", "tijera"]

        if jug1 not in opciones or jug2 not in opciones:
            return "invalid"  

        if jug1 == jug2:
            return "empate"

        if (jug1 == "piedra" and jug2 == "tijera") or \
           (jug1 == "papel" and jug2 == "piedra") or \
           (jug1 == "tijera" and jug2 == "papel"):
            return "jugador1"
        else:
            return "jugador2"

    def adivinar_numero_pista(self, numero, secreto):
        if numero == secreto:
            return "correcto"
        elif numero > secreto:
            return "muy alto"   
        else:
            return "muy bajo"  

    def ta_te_ti_ganador(self, tablero):
    
        for i in range(3):
            if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
                return tablero[i][0]
            if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
                return tablero[0][i]

    
        if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
            return tablero[0][0]
        if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
            return tablero[0][2]

 
        for fila in tablero:
            if " " in fila:
                return "continua"
        return "empate"

    def validar_movimiento_torre_ajedrez(self, x1, y1, x2, y2, tablero):
    
        if not (0 <= x1 < 8 and 0 <= y1 < 8 and 0 <= x2 < 8 and 0 <= y2 < 8):
            return False
        if x1 == x2 and y1 == y2:
            return False
        if x1 != x2 and y1 != y2:
            return False

       
        if x1 == x2:  
            paso = 1 if y2 > y1 else -1
            for y in range(y1 + paso, y2, paso):
                if tablero[x1][y] != " ":
                    return False
        else: 
            paso = 1 if x2 > x1 else -1
            for x in range(x1 + paso, x2, paso):
                if tablero[x][y1] != " ":
                    return False

        return True