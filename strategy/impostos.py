# -*- coding: utf-8 -*-

from abc import ABCMeta, abstractmethod

class Imposto(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def calcula(self, orcamento):
        """
        Calcula o imposto a partir de um orcamento.
        :param orcamento: objeto da classe Orcamento com o valor para ser calculado.
        """
        return orcamento.valor * 0.005


class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1


class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06


class IPI(Imposto):
    def calcula(self, orcamento):
        return super(IPI, self).calcula(orcamento)

    def __str__(self):
        print 'IPI'
