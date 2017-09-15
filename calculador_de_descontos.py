# -*- coding: utf-8 -*-

class CalculadoraDeDescontos(object):
    """
    Define o método para cálculo de Descontos dado um orçamento.
    """
    def calcula(self, orcamento):
        """
        Efetua o cálculo de descontos.
        :param orcamento: objeto da classe Orcamento contendo valor para ser calculado.
        """
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1

        elif orcamento.valor > 500:
            return orcamento.valor * 0.07
