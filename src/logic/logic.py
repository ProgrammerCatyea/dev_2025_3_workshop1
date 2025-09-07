class Logica:

    
    def AND(self, ar, b):
        resultado = (ar and b)
        return bool(resultado)
    
    def OR(self, ar, b):
        resultado = ar or b
        return bool(resultado)
    
    def NOT(self, ar):
        return not ar
    
    def XOR(self, ar, b):
        return ar != b
    
    def NAND(self, ar, b):
        return not (ar and b)
    
    def NOR(self, ar, b):
        return not (ar or b)
    
    def XNOR(self, ar, b):
        return ar == b
    
    def implicacion(self, ar, b):
        return (not ar) or b
    
    def bi_implicacion(self, ar, b):
        return ar== b