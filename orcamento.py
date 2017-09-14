# -*- coding: utf-8 -*-

class Orcamento(object):
    """
    Armazena um orçamento, cálculo ou estimativa de custos.
    """
    def __init__(self, valor):
        self.__valor = valor

    @property
    def valor(self):
        """
        Getter para a propriedade valor.
        """
        return self.__valor
