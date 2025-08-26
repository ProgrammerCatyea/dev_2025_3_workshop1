class Data:

    def invertir_lista(self, lista):
        invertida = []
        for i in range(len(lista) - 1, -1, -1):
            invertida.append(lista[i])
        return invertida
        pass
    
    def buscar_elemento(self, lista, elemento):
        for i in range(len(lista)):
            if lista[i] == elemento:
                return i
        return -1
        pass
    
    def eliminar_duplicados(self, lista):
        nueva = []
        for elem in lista:
            if elem not in nueva:
                nueva.append(elem)
        return nueva
        pass
    
    def merge_ordenado(self, lista1, lista2):
        i, j = 0, 0
        resultado = []
        while i < len(lista1) and j < len(lista2):
            
            if lista1[i] <= lista2[j]:
                resultado.append(lista1[i])
                i += 1

            else:
                resultado.append(lista2[j])
                j += 1
        while i < len(lista1):

            resultado.append(lista1[i])
            i += 1
        while j < len(lista2):
            resultado.append(lista2[j])
            j += 1

        return resultado
        pass
    
    def rotar_lista(self, lista, k):
        if not lista:
            return lista
        k = k % len(lista)  
        return lista[-k:] + lista[:-k]
        pass
    
    def encuentra_numero_faltante(self, lista):
        n = len(lista) + 1
        esperado = n * (n + 1) // 2
        real = sum(lista)
        return esperado - real
        pass
    
    def es_subconjunto(self, conjunto1, conjunto2):
        for elem in conjunto1:
            if elem not in conjunto2:
                return False
        return True
        pass
    
    def implementar_pila(self):
        pila = []
        return {
            "push": lambda x: pila.append(x),
            "pop": lambda: pila.pop() if pila else None,
            "peek": lambda: pila[-1] if pila else None,
            "is_empty": lambda: len(pila) == 0
        }
        pass
    
    def implementar_cola(self):
        cola = []
        return {
            "enqueue": lambda x: cola.append(x),
            "dequeue": lambda: cola.pop(0) if cola else None,
            "peek": lambda: cola[0] if cola else None,
            "is_empty": lambda: len(cola) == 0
        }
        pass
    
    def matriz_transpuesta(self, matriz):
        filas = len(matriz)
        columnas = len(matriz[0]) if matriz else 0
        transpuesta = []
        for j in range(columnas):
            fila = []
            for i in range(filas):
                fila.append(matriz[i][j])
            transpuesta.append(fila)
        return transpuesta
        pass