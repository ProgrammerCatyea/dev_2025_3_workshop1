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