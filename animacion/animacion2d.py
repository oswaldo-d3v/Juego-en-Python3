from animacion import Iteradores


class Animacion2D():

    def generar_anamcion(self, posicion_inicial, fotogramas, forma=None):
        iterador = Iteradores(fotogramas, (6, 6))

        def anmacion():
            return iterador.get_posicion(posicion_inicial)
        return anmacion

    pass
