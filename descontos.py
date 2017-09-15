# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod


class Desconto(object):
    __metaclass__ = ABCMeta

    def __init__(self, proximo_desconto=None):
        self.__proximo_desconto = proximo_desconto

    @abstractmethod
    def calcula(self, orcamento):
        """
        Calcula um desconto a partir de um orcamento e chama o próximo desconto caso não atenda a condição.
        :param orcamento: objeto da classe Orcamento com o valor para ser calculado.
        """
        pass
    
    @property
    def proximo_desconto(self):
        """
        Getter do atributo próximo desconto.
        """
        return self.__proximo_desconto


class DescontoPorCincoItens(Desconto):

    def calcula(self, orcamento):
        if orcamento.total_itens >= 5:
            return orcamento.valor * 0.1

        elif self.proximo_desconto is not None:
            return self.__proximo_desconto.calcula(orcamento)


class DescontoPorMaisDeQuinhentosReais(Desconto):
    
    def calcula(self, orcamento):
        if orcamento.valor > 500.00:
            return orcamento.valor * 0.07

        elif self.proximo_desconto is not None:
            return self.__proximo_desconto.calcula(orcamento)
