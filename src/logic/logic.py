class Logica:

    
    def AND(self, a, b):
        resultado = (a and b)
        return bool(resultado)
    
    def OR(self, a, b):
        resultado = a or b
        return bool(resultado)
    
    def NOT(self, a):
        return not a
    
    def XOR(self, a, b):
        return a != b
    
    def NAND(self, a, b):
        return not (a and b)
    
    def NOR(self, a, b):
        return not (a or b)
    
    def XNOR(self, a, b):
        return a == b
    
    def implicacion(self, a, b):
        return (not a) or b
    
    def bi_implicacion(self, a, b):
        return a == b