# -*- coding: utf-8 -*-
from descontos import DescontoPorCincoItens, DescontoPorMaisDeQuinhentosReais, SemDesconto

class CalculadorDeDescontos(object):
    """
    Define o método para cálculo de Descontos dado um orçamento.
    """
    def calcula(self, orcamento):
        """
        Efetua o cálculo de descontos.
        :param orcamento: objeto da classe Orcamento contendo valor para ser calculado.
        """
        desconto = DescontoPorCincoItens(
            DescontoPorMaisDeQuinhentosReais(SemDesconto())
            ).calcula(orcamento)
        
        return desconto


if __name__ == '__main__':
    from orcamento import Item, Orcamento

    orcamento = Orcamento()
    orcamento.adiciona_item(Item('ITEM - 1', 100.0))
    orcamento.adiciona_item(Item('ITEM - 2', 50.0))
    orcamento.adiciona_item(Item('ITEM - 3', 100.0))

    calculador = CalculadorDeDescontos()

    desconto = calculador.calcula(orcamento)
    print '{}%'.format(desconto)
