class Iteradores():

    def __es_posicion_validad(self, posicion):
        out = (self.total_columnas >= posicion[0]) and (posicion[0] >= 0)
        out = out and (self.total_filas >= posicion[1]) and (posicion[1] >= 0)
        return out

    def __es_ultimo_fotograma(self):
        return self.fotograma_actual == self.total_fotogramas

    def __iterar_fotograma(self):
        if not self.__es_ultimo_fotograma():
            self.fotograma_actual += 1
        else:
            self.fotograma_actual = 0

    def __iterar_en_matriz(self):
        if self.columna_actual < self.total_columnas:
            self.columna_actual += 1
        else:
            self.columna_actual = 0
            if self.fila_actual < self.total_filas:
                self.fila_actual += 1
            else:
                self.fila_actual = 0

    def get_posicion(self, posicion_inicial):
        if not self.__es_posicion_validad(posicion_inicial):
            raise ValueError('La posicion no existe en la matriz.')
        if not self.fotograma_actual == 0:
            self.__iterar_en_matriz()
        else:
            self.columna_actual = posicion_inicial[0]
            self.fila_actual = posicion_inicial[1]
        self.__iterar_fotograma()
        return self.columna_actual, self.fila_actual

    def __init__(self, fotogramas, forma):
        self.total_fotogramas = fotogramas - 1
        self.total_columnas = forma[0] - 1
        self.total_filas = forma[1] - 1

        self.fotograma_actual = 0


if __name__ == "__main__":
    iterador = Iteradores(8, (6, 6))
    for i in range(24):
        print(iterador.get_posicion((4, 5)))
