class Conjunto:
    def __init__(self, conjunto, pesos=None):
        self.__conjunto = conjunto
        self.__pesos = pesos

    def promedio(self):

        if len(self.__conjunto) == 1:
            return (self.__conjunto[0])

        else:
            return None

