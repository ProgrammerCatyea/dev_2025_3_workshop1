class Strings:

    def es_palindromo(self, texto):
        limpio = ''.join(ch.lower() for ch in texto if ch.isalnum())
        return limpio == limpio[::-1]

    def invertir_cadena(self, texto):
        invertida = ""
        for i in range(len(texto) - 1, -1, -1):
            invertida += texto[i]
        return invertida

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
        return " ".join(p[0].upper() + p[1:] if p else "" for p in texto.split(" "))

    def eliminar_espacios_duplicados(self, texto):
        resultado = ""
        ultimo = ""
        for ch in texto:
            if ch == " " and ultimo == " ":
                continue
            resultado += ch
            ultimo = ch
        return resultado.strip()

    def es_numero_entero(self, texto):
        if texto.startswith("-"):
            texto = texto[1:]
        if not texto:
            return False
        return all("0" <= ch <= "9" for ch in texto)

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
        posiciones = []
        for i in range(len(texto) - len(subcadena) + 1):
            if texto[i:i+len(subcadena)] == subcadena:
                posiciones.append(i)
        return posiciones