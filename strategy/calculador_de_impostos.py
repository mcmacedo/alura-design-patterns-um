# -*- coding: utf-8 -*-

from impostos import ISS, ICMS, IPI

class CalculadorDeImpostos(object):
    """
    Define o método para o cálculo de impostos com base em um orcamento.
    """
    def realiza_calculo(self, orcamento, imposto):
        """
        Efetua o cálculo de impostos.
        :param orcamento: objeto da classe Orcamento contendo valor para ser calculado.
        :param imposto: objeto imposto com a regra de imposto que deve ser aplicado.
        """
        imposto_calculado = imposto.calcula(orcamento)

        print imposto_calculado


if __name__ == '__main__':
    from orcamento import Orcamento

    calculador = CalculadorDeImpostos()
    orcamento = Orcamento(500)

    calculador.realiza_calculo(orcamento, ISS())
    calculador.realiza_calculo(orcamento, ICMS())
    calculador.realiza_calculo(orcamento, IPI())
