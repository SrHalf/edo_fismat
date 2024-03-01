# -*- coding: utf-8 -*-
import numbers

class Populacao:
    def __init__(self, inicial):
        if not isinstance(inicial, numbers.Number):
            raise TypeError("Somente números são permitidos.")
        self.inicial = inicial

class Presa(Populacao):
    """
        Representa uma presa qualquer.
    """
    pass

class Predador(Populacao):
    pass
