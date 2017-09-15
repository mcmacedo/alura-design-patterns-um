# -*- coding: utf-8 -*-

class DescontoPorCincoItens(object):

    def calcula(self, orcamento):
        if orcamento.total_itens > 5:
            return orcamento.valor * 0.1
        else:
            return 0


class DescontoPorMaisDeQuinhentosReais(object):
    
    def calcula(self, orcamento):
        if orcamento.valor > 500.00:
            return orcamento.valor * 0.07
        else:
            return 0
