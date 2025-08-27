class Magic:

    def fibonacci(self, n, memo=None):
        if memo is None:
            memo = {}
        if n in memo:
            return memo[n]
        if n <= 1:
            return n
        memo[n] = self.fibonacci(n-1, memo) + self.fibonacci(n-2, memo)
        return memo[n]

    def secuencia_fibonacci(self, n):
        if n <= 0:
            return []
        if n == 1:
            return [0]
        sec = [0, 1]
        while len(sec) < n:
            sec.append(sec[-1] + sec[-2])
        return sec[:n]

    def es_primo(self, n):
        if n < 2:
            return False
        if n in (2, 3):
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False
        return True

    def generar_primos(self, n):
        return [x for x in range(2, n+1) if self.es_primo(x)]

    def es_numero_perfecto(self, n):
        if n < 2:
            return False
        suma_div = 1
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                suma_div += i
                if i != n // i:
                    suma_div += n // i
        return suma_div == n

    def triangulo_pascal(self, filas):
        if filas <= 0:
            return []
        tri = [[1]]
        for _ in range(1, filas):
            fila = [1]
            for j in range(1, len(tri[-1])):
                fila.append(tri[-1][j-1] + tri[-1][j])
            fila.append(1)
            tri.append(fila)
        return tri

    def factorial(self, n):
        if n < 0:
            raise ValueError("El factorial no está definido para números negativos")
        res = 1
        for i in range(2, n+1):
            res *= i
        return res

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return abs(a)

    def mcm(self, a, b):
        if a == 0 or b == 0:
            return 0
        return abs(a*b) // self.mcd(a, b)

    def suma_digitos(self, n):
        s = 0
        n = abs(n)
        while n > 0:
            s += n % 10
            n //= 10
        return s

    def es_numero_armstrong(self, n):
        digitos = [int(d) for d in str(abs(n))]
        potencia = len(digitos)
        return sum(d**potencia for d in digitos) == abs(n)

    def es_cuadrado_magico(self, matriz):
        n = len(matriz)
        if n == 0 or any(len(fila) != n for fila in matriz):
            return False
        
        suma_ref = sum(matriz[0])
        

        for i in range(n):
            if sum(matriz[i]) != suma_ref or sum(matriz[j][i] for j in range(n)) != suma_ref:
                return False
        
    
        if sum(matriz[i][i] for i in range(n)) != suma_ref:
            return False
        
        if sum(matriz[i][n-1-i] for i in range(n)) != suma_ref:
            return False
        
        return True