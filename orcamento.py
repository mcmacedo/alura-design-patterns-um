# -*- coding: utf-8 -*-

class Orcamento(object):
    """
    Representa um orçamento formado por uma lista de items.
    """
    def __init__(self):
        self.__itens = []

    @property
    def valor(self):
        """
        Retorna a soma dos valores dos itens do orçamento. 
        """
        total = 0.0
        for item in self.__itens:
            total += item.valor
        return total

    @property
    def total_itens(self):
        """
        Retorna quantidade de itens do orçamento.
        """
        return len(self.__itens)

    def obter_itens(self):
        """
        Retorna tupla com os itens do orçamento.
        """
        return tuple(self.__itens)

    def adiciona_item(self, item):
        """
        Adiciona um item ao orçamento
        """
        self.__itens.append(item)

class Item(object):
    """
    Item ou produto.
    """
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    @property
    def valor(self):
        """
        Getter do atributo valor.
        """
        return self.__valor

    @property
    def nome(self):
        """
        Getter do atributo nome.
        """
        return self.__nome
