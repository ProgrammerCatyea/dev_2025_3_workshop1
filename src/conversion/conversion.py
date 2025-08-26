class Conversion:
    def celsius_a_fahrenheit(self, celsius):
        return (celsius * 9/5) + 32
    
    def fahrenheit_a_celsius(self, fahrenheit):
        return (fahrenheit - 32) * 5/9
    
    def metros_a_pies(self, metros):
        return metros * 3.281
    
    def pies_a_metros(self, pies):
        return pies / 3.281

    def decimal_a_binario(self, decimal):
        if decimal == 0:
            return "0"
        binario = ""  
        while decimal > 0:
            resto = decimal % 2
            binario = str(resto) + binario
            decimal //= 2
        return binario.strip()  
    
    def binario_a_decimal(self, binario):
        decimal = 0
        for i, digito in enumerate(binario[::-1]):
            if digito == "1":
                decimal += 2 ** i
        return decimal
    
    def decimal_a_romano(self, numero):
        valores = 
        [
            (900, "CM"), (1000, "M"), (400, "CD"), (500, "D"),
            (90, "XC"), (100, "C"), (40, "XL"), (50, "L"),
            (9, "IX"), (10, "X"), (4, "IV"), (5, "V"),
            (1, "I")
        ]
        romano = ""
        for valor, simbolo in valores:
            while numero >= valor:
                romano += simbolo
                numero -= valro
        return romano
    
    def romano_a_decimal(self, romano):
        valores = {"I": 1, "V": 5, "X": 10, "L": 50,
                   "C": 100, "D": 500, "M": 1000}
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
    
    def texto_a_morse(self, texto):
        morse_dict = 
        {
            "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
            "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
            "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
            "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
            "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
            "Z": "--..",
            "0": "-----", "1": ".----", "2": "..---", "3": "...--",
            "4": "....-", "5": ".....", "6": "-....", "7": "--...",
            "8": "---..", "9": "----."
        }
        texto = texto.upper()
      
        return " / ".join(morse_dict[ch] for ch in texto if ch in morse_dict)
    
    def morse_a_texto(self, morse):
        morse_dict = 
        {
            ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E",
            "..-.": "F", "--.": "G", "....": "H", "..": "I", ".---": "J",
            "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O",
            ".--.": "P", "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
            "..-": "U", "...-": "V", ".--": "W", "-..-": "X", "-.--": "Y",
            "--..": "Z",
            "-----": "0", ".----": "1", "..---": "2", "...--": "3",
            "....-": "4", ".....": "5", "-....": "6", "--...": "7",
            "---..": "8", "----.": "9"
        }
        
        letras = morse.replace("/", " ").split()
        return "".join(morse_dict[c] for c in letras if c in morse_dict)