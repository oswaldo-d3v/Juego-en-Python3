class Iteradores():

    def __init__(self, fotogramas, forma):
        self.total_fotogramas = fotogramas - 1
        self.total_columnas = forma[0] - 1
        self.total_filas = forma[1] - 1

        self.fotograma_actual = 0
        self.columna_actual = 0
        self.fila_actual = 0
