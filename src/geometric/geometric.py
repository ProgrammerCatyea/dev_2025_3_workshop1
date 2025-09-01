import math

class Geometria:

    def es_triangulo_valido(self, a: float, b: float, c: float) -> bool:
        return a + b > c and a + c > b and b + c > a
    def area_cuadrado(self, lado: float) -> float:
        return lado ** 2

    def area_rectangulo(self, base: float, altura: float) -> float:
        return base * altura

    def area_triangulo(self, base: float, altura: float) -> float:
        return (base * altura) / 2

    def area_circulo(self, radio: float) -> float:
        return math.pi * (radio ** 2)

    def area_trapecio(self, base_mayor: float, base_menor: float, altura: float) -> float:
        return ((base_mayor + base_menor) * altura) / 2

    def area_rombo(self, d1: float, d2: float) -> float:
        return (d1 * d2) / 2

    def area_pentagono_regular(self, lado: float, apotema: float) -> float:
        return (5 * lado * apotema) / 2

    def area_hexagono_regular(self, lado: float, apotema: float) -> float:
        return (6 * lado * apotema) / 2

    def area_poligono_regular(self, n: int, lado: float, apotema: float) -> float:
        
        if n < 3:
            raise ValueError("Un polígono debe tener al menos 3 lados.")
        perimetro = n * lado
        area = (perimetro * apotema) / 2
        
        if n == 4:
            return perimetro * apotema
        return area

    def perimetro_cuadrado(self, lado: float) -> float:
        return 4 * lado

    def perimetro_rectangulo(self, base: float, altura: float) -> float:
        return 2 * (base + altura)

    def perimetro_triangulo(self, lado1: float, lado2: float, lado3: float) -> float:
        return lado1 + lado2 + lado3

    def perimetro_circulo(self, radio: float) -> float:
        return 2 * math.pi * radio

    def perimetro_pentagono_regular(self, lado: float) -> float:
        return 5 * lado

    def perimetro_hexagono_regular(self, lado: float) -> float:
        return 6 * lado

    def perimetro_poligono_regular(self, n: int, lado: float) -> float:
        return n * lado

    def volumen_cubo(self, lado: float) -> float:
        return lado ** 3

    def area_superficie_cubo(self, lado: float) -> float:
        return 6 * (lado ** 2)

    def volumen_esfera(self, radio: float) -> float:
        return (4/3) * math.pi * (radio ** 3)

    def area_superficie_esfera(self, radio: float) -> float:
        return 4 * math.pi * (radio ** 2)

    def volumen_cilindro(self, radio: float, altura: float) -> float:
        return math.pi * (radio ** 2) * altura

    def area_superficie_cilindro(self, radio: float, altura: float) -> float:
        return 2 * math.pi * radio * (radio + altura)

    def distancia_entre_puntos(self, x1: float, y1: float, x2: float, y2: float) -> float:
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def punto_medio(self, x1: float, y1: float, x2: float, y2: float) -> tuple:
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def pendiente_recta(self, x1: float, y1: float, x2: float, y2: float) -> float:
        if x2 - x1 == 0:
            raise ZeroDivisionError("Pendiente indefinida (recta vertical)")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1: float, y1: float, x2: float, y2: float) -> tuple:
       
        A = y2 - y1
        B = x1 - x2
        C = x2 * y1 - x1 * y2

        if A == 0 and B != 0:
            B = 1
            C = -y1
        elif B == 0 and A != 0:
  
            A = 1
            C = -x1
        else:
            if A < 0 or (A == 0 and B < 0):
                A, B, C = -A, -B, -C
            from math import gcd
            g = gcd(gcd(int(A), int(B)), int(C)) if all(float(v).is_integer() for v in (A, B, C)) else 1
            if g > 1:
                A //= g
                B //= g
                C //= g
        return (A, B, C)
    def angulo_entre_rectas(self, m1: float, m2: float) -> float:
        if 1 + (m1 * m2) == 0:
            return 90.0
        angulo_rad = math.atan(abs((m1 - m2) / (1 + m1 * m2)))
        return math.degrees(angulo_rad)
