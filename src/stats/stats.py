class Stats:
    def promedio(self, numeros):
        
        if not numeros:  # lista vacía
            return None
        suma = 0
        for n in numeros:
            suma += n
        prom = suma / len(numeros)
        return prom
    
    def mediana(self, numeros):
        
        if not numeros:
            return None
        valores = sorted(numeros)
        n_datos = len(valores)
        mitad = n_datos // 2
        if n_datos % 2 == 0:  # par
            return (valores[mitad - 1] + valores[mitad]) / 2
        else:  # impar
            return valores[mitad]
    
    def moda(self, numeros):
        
        if not numeros:
            return None
        conteo = {}
        for num in numeros:
            conteo[num] = conteo.get(num, 0) + 1
        mas_repetido = None
        veces = 0
        for k, v in conteo.items():
            if v > veces:
                mas_repetido = k
                veces = v
        return mas_repetido
    
    def desviacion_estandar(self, numeros):
        
        if not numeros:
            return None
        media = self.promedio(numeros)
        suma_cuadrados = 0
        for x in numeros:
            suma_cuadrados += (x - media) ** 2
        var = suma_cuadrados / len(numeros)
        return var ** (1/2)  # en vez de math.sqrt(var)
    
    def varianza(self, numeros):
        """
        Calcula la varianza de una lista de números.
        """
        if not numeros:
            return None
        media = self.promedio(numeros)
        suma = 0
        for x in numeros:
            suma += (x - media) ** 2
        return suma / len(numeros)
    
    def rango(self, numeros):
        """
        Calcula el rango de un conjunto.
        """
        if not numeros:
            return None
        maximo = max(numeros)
        minimo = min(numeros)
        return maximo - minimo