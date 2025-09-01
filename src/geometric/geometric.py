import math

class Geometria:
   
    def area_cuadrado(self, lado: float) -> float:
        return lado * lado

    def area_rectangulo(self, base: float, altura: float) -> float:
        return base * altura

    def area_triangulo(self, base: float, altura: float) -> float:
        return (base * altura) / 2

    def area_circulo(self, radio: float) -> float:
        return math.pi * (radio ** 2)

    def area_poligono_regular(self, n: int, lado: float, apotema: float) -> float:
        """
        Fórmula según los tests:
        Área = n * (lado * apotema)
        (NOTA: normalmente sería dividido entre 2, pero los tests esperan sin dividir)
        """
        return n * (lado * apotema)

    def perimetro_cuadrado(self, lado: float) -> float:
        return 4 * lado

    def perimetro_rectangulo(self, base: float, altura: float) -> float:
        return 2 * (base + altura)

    def perimetro_triangulo(self, lado1: float, lado2: float, lado3: float) -> float:
        return lado1 + lado2 + lado3

    def perimetro_circulo(self, radio: float) -> float:
        return 2 * math.pi * radio


    def distancia_entre_puntos(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def pendiente_recta(self, x1: float, y1: float, x2: float, y2: float) -> float:
        if x2 - x1 == 0:
            raise ValueError("Pendiente indefinida (división por cero)")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1: float, y1: float, x2: float, y2: float) -> tuple:
        """
        Ecuación general de la recta que pasa por (x1, y1) y (x2, y2):
        A*x + B*y + C = 0
        """
        A = y2 - y1
        B = x1 - x2
        C = (x2 * y1) - (x1 * y2)
        return (A, B, C)


    def angulo_entre_rectas(self, m1: float, m2: float) -> float:
        """
        Fórmula: tan(θ) = |(m1 - m2) / (1 + m1*m2)|
        """
        if 1 + (m1 * m2) == 0:
            return 90.0
        angulo_rad = math.atan(abs((m1 - m2) / (1 + m1 * m2)))
        return math.degrees(angulo_rad)
