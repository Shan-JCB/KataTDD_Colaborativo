class Conjunto:
    def __init__(self, conjunto, pesos=None):
        self.__conjunto = conjunto
        self.__pesos = pesos

    def promedio(self):
        if not self.__conjunto:  # Verifica si el conjunto está vacío
            return None
        if not self.__pesos:  # Si no hay pesos, calcula el promedio simple
            return sum(self.__conjunto) / len(self.__conjunto)

        total_peso = sum(self.__pesos)
        if total_peso == 0:
            return None  # Evitar división por cero

        promedio_ponderado = sum(x * w for x, w in zip(self.__conjunto, self.__pesos)) / total_peso
        return round(promedio_ponderado, 2)