class Strings:

    def es_palindromo(self, texto):
        limpio = ''.join(ch.lower() for ch in texto if ch.isalnum())
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        return texto[::-1]

    def contar_vocales(self, texto):
        vocales = "aeiouáéíóú"
        return sum(1 for ch in texto.lower() if ch in vocales)

    def contar_consonantes(self, texto):
        vocales = "aeiouáéíóú"
        return sum(1 for ch in texto.lower() if ch.isalpha() and ch not in vocales)

    def es_anagrama(self, texto1, texto2):
        t1 = sorted(texto1.replace(" ", "").lower())
        t2 = sorted(texto2.replace(" ", "").lower())
        return t1 == t2

    def contar_palabras(self, texto):
        palabras = [p for p in texto.split(" ") if p.strip() != ""]
        return len(palabras)

    def palabras_mayus(self, texto):
        return " ".join(p.capitalize() for p in texto.split(" "))

    def eliminar_espacios_duplicados(self, texto):
        import re
        return re.sub(r' +', ' ', texto)

    def es_numero_entero(self, texto):
        texto = texto.strip()
        if texto.startswith("-"):
            texto = texto[1:]
        if not texto:
            return False
        return texto.isdigit()

    def cifrar_cesar(self, texto, desplazamiento):
        resultado = ""
        for ch in texto:
            if ch.isalpha():
                base = 65 if ch.isupper() else 97
                resultado += chr((ord(ch) - base + desplazamiento) % 26 + base)
            else:
                resultado += ch
        return resultado

    def descifrar_cesar(self, texto, desplazamiento):
        return self.cifrar_cesar(texto, -desplazamiento)

    def encontrar_subcadena(self, texto, subcadena):
        if not subcadena:
            return []
        posiciones = []
        i = texto.find(subcadena)
        while i != -1:
            posiciones.append(i)
            i = texto.find(subcadena, i + 1)
        return posiciones