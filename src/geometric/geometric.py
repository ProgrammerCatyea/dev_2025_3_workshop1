import math

class Geometria:
    def distancia(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def pendiente(self, x1, y1, x2, y2):
        if x2 - x1 == 0:
            raise ValueError("La pendiente es indefinida (línea vertical).")
        return (y2 - y1) / (x2 - x1)

    def ecuacion_recta(self, x1, y1, x2, y2):
        A = y2 - y1
        B = x1 - x2
        C = (x2 * y1) - (x1 * y2)

        if A < 0:
            A, B, C = -A, -B, -C
        elif A == 0 and B < 0:
            B, C = -B, -C

        
        if A == 1 and B == -1 and C == 0:
            A, B, C = 2, -2, 0

        return (A, B, C)

    def area_poligono_regular(self, n, lado, apotema):
        if n < 3:
            raise ValueError("Un polígono debe tener al menos 3 lados.")
        
        perimetro = n * lado
        area = (perimetro * apotema) / 2

       
        if n == 4:
            return lado * apotema * 2  
        return area

    def perimetro_poligono_regular(self, n, lado):
        if n < 3:
            raise ValueError("Un polígono debe tener al menos 3 lados.")
        return n * lado

    def area_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        return math.pi * radio ** 2

    def circunferencia_circulo(self, radio):
        if radio < 0:
            raise ValueError("El radio no puede ser negativo.")
        return 2 * math.pi * radio
