class Iteradores():
    def iterar_fotograma(self):
        if self.__iterador_fotograma < self.__fotogramas:
            self.__iterador_fotograma += 1
        else:
            self.__iterador_fotograma = 0

    def iterar_matriz(self):
        if self.__iterador_columnas < self.__maximo_columnas:
            self.__iterador_columnas += 1
        else:
            self.__iterador_columnas = 0
            if self.__iterador_filas < self.__maximo_filas:
                self.__iterador_filas += 1
            else:
                self.__iterador_filas = 0

    def generar_iterable(self, inicio, fotogramas):
        self.__fotogramas = fotogramas - 1

        def get_posicion(self):
            if self.__iterador_fotograma > 0:
                self.iterar_matriz()
            else:
                self.__iterador_columnas = inicio[0]
                self.__iterador_filas = inicio[1]
            self.iterar_fotograma()
            return self.__iterador_columnas, self.__iterador_filas
        return get_posicion

    def __init__(self, forma):
        self.__maximo_columnas = forma[0] - 1
        self.__maximo_filas = forma[1] - 1

        self.__iterador_fotograma = 0
    pass


matriz = Iteradores((5, 5))
correr_derecha = matriz.generar_iterable((1, 3), 12)

for i in range(12):
    print(correr_derecha(matriz))
