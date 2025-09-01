class Conversion:
    def __init__(self):
        pass


    def metros_a_pies(self, metros):
        return metros * 3.28084

    def pies_a_metros(self, pies):
        return pies * 0.3048

    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32

    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9

    def texto_a_morse(self, texto):
        MORSE = {
            'A': '.-',   'B': '-...', 'C': '-.-.', 'D': '-..',  'E': '.',
            'F': '..-.', 'G': '--.',  'H': '....', 'I': '..',   'J': '.---',
            'K': '-.-',  'L': '.-..', 'M': '--',   'N': '-.',   'O': '---',
            'P': '.--.', 'Q': '--.-', 'R': '.-.',  'S': '...',  'T': '-',
            'U': '..-',  'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',
            'Z': '--..',
            '0': '-----','1': '.----','2': '..---','3': '...--','4': '....-',
            '5': '.....','6': '-....','7': '--...','8': '---..','9': '----.'
        }
        tokens = []
        for ch in texto.upper():
            if ch == ' ':
                tokens.append('/')
            elif ch in MORSE:
                tokens.append(MORSE[ch])
        return ' '.join(tokens)

    def morse_a_texto(self, morse):
        INV = {
            '.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
            '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
            '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z',
            '-----':'0','.----':'1','..---':'2','...--':'3','....-':'4','.....':'5','-....':'6','--...':'7','---..':'8','----.':'9'
        }
        resultado = []
        for tok in morse.split(' '):
            if tok == '':
                continue
            if tok == '/':
                resultado.append(' ')
            else:
                resultado.append(INV.get(tok, ''))
        return ''.join(resultado)

    def decimal_a_binario(self, numero):
        if numero == 0:
            return "0"
        binario = ""
        n = numero
        while n > 0:
            binario = str(n % 2) + binario
            n //= 2
        return binario

    def binario_a_decimal(self, binario):
        return int(binario, 2)

    def decimal_a_romano(self, numero):
        valores = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
            (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
            (1, 'I')
        ]
        resultado = ""
        n = numero
        for val, simbolo in valores:
            while n >= val:
                resultado += simbolo
                n -= val
        return resultado

    def romano_a_decimal(self, romano):
        valores = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        total = 0
        i = 0
        while i < len(romano):
            if i+1 < len(romano) and valores[romano[i]] < valores[romano[i+1]]:
                total += valores[romano[i+1]] - valores[romano[i]]
                i += 2
            else:
                total += valores[romano[i]]
                i += 1
        return total