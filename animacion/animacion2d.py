'''Generar atributo sprite para obtener su ancho y alto en base a la forma'''
from animacion import Iteradores


class Animacion2D():

    def __calcular_cordenada(self, posicion):
        return posicion[0] * 1, posicion[1] * 1

    def __es_posicion_validad(self, posicion, iterador):
        out = (iterador.total_columnas >= posicion[0]) and (posicion[0] >= 0)
        out = out and (iterador.total_filas >= posicion[1])
        out = out and (posicion[1] >= 0)
        return out

    def __iterar_fotograma(self, iterador):
        es_ultimo_fotograma = (
            iterador.fotograma_actual == iterador.total_fotogramas
        )
        if not es_ultimo_fotograma:
            iterador.fotograma_actual += 1
        else:
            iterador.fotograma_actual = 0

    def __iterar_en_matriz(self, iterador):
        if iterador.columna_actual < iterador.total_columnas:
            iterador.columna_actual += 1
        else:
            iterador.columna_actual = 0
            if iterador.fila_actual < iterador.total_filas:
                iterador.fila_actual += 1
            else:
                iterador.fila_actual = 0

    def __generar_iterador(self, posicion_inicial, fotogramas, forma=None):
        iterador = Iteradores(fotogramas, (6, 6))

        def get_posicion():
            if not self.__es_posicion_validad(posicion_inicial, iterador):
                raise ValueError('La posicion no existe en la matriz.')
            if not iterador.fotograma_actual == 0:
                self.__iterar_en_matriz(iterador)
            else:
                iterador.columna_actual = posicion_inicial[0]
                iterador.fila_actual = posicion_inicial[1]
            self.__iterar_fotograma(iterador)
            return iterador.columna_actual, iterador.fila_actual
        return get_posicion

    def generar_animacion(self, posicion_inicial, fotogramas, forma=None):
        get_posicion = self.__generar_iterador(
            posicion_inicial, fotogramas, forma)

        def animacion():
            posicion = get_posicion()
            cordenada = self.__calcular_cordenada(posicion)
            # Crear rectangulo
            # Crear subare
            # Devolver subarea
            return posicion
        return animacion

    pass
