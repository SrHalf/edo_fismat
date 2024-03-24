# -*- coding: utf-8 -*-
import numbers
import math
import modelos


class Sistema:
    """
        Representa um sistema sem capacidade de carga, limiar ou predador.
        A representação gráfica mostra o crescimento indefinido de P.
        dP/dt = rP --> P(t) = Ae^(rt).
    """

    def __init__(self, populacao):
        if not isinstance(populacao, modelos.Populacao):
            raise TypeError("O parâmetro não é um objeto População.")
        self.populacao = populacao

    def p(self, t, r):
        """
            Avalia P(t).
        """
        return self.populacao.inicial * math.exp(r * t)


class SistemaK(Sistema):
    """
        Representa um sistema com capacidade de carga, K.
        dP/dt = rP(1 -P/K)
    """

    def __init__(self, populacao, capacidade):
        super().__init__(populacao)
        if not isinstance(capacidade, numbers.Number):
            raise TypeError("Somente números são permitidos.")
        self.capacidade = capacidade

    def p(self, t, r):
        """
            Avalia P(t).
        """
        return (self.populacao.inicial * self.capacidade * math.exp(r * t)) / \
            ((self.capacidade - self.populacao.inicial) + self.populacao.inicial * math.exp(r * t))


class SistemaKT(SistemaK):
    """
        Representa um sistema com capacidade de carga e limiar, K e T;
        dP/dt = rP(1 -P/K)(1 -P/T)
    """

    def __init__(self, populacao, capacidade, limiar):
        super().__init__(populacao, capacidade)
        if not isinstance(limiar, numbers.Number):
            raise TypeError("Somente números são permitidos.")
        self.limiar = limiar

    def p(self, t, r=0.18):
        """
            Avalia P(t).
            A variável r é a taxa percentual de crescimento.
            O valor de 18% foi especificado pelos exemplos seguidos nas referências,
            mas deve ser alterado para se adequar a problemas diferentes.
        """
        return (self.capacidade * self.limiar) / \
            (1 + ((self.capacidade - self.limiar) / self.limiar) * math.exp(-r * t))


class SistemaXY:
    """
        Representa um sistema predador-presa.
        dy/dx = (y(dx -c)) / (x(a -by))
    """
    pass
