import modelos
import sistemas
import matplotlib.pyplot as plt
import numpy as np


def simular_sistema_slimite(p0, taxa, limitacao):
    populacao = modelos.Populacao(p0)
    sistema = sistemas.Sistema(populacao)

    plt.ion()
    ts = []
    ps = []
    for i in range(limitacao):
        ts.append(i)
        ps.append(sistema.p(i, taxa))
        xs = np.array(ts)
        ys = np.array(ps)
        plt.plot(xs, ys)
        plt.title("Cresc. Populacional Sem Limite")
        plt.xlabel("Tempo (t)")
        plt.ylabel("População (P)")
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a, b)
    plt.title("Cresc. Populacional Sem Limite")
    plt.xlabel("Tempo (t)")
    plt.ylabel("População (P)")
    plt.show()


def simular_sistema_k(p0, r, k, limitacao):
    populacao = modelos.Populacao(p0)
    sistema = sistemas.SistemaK(populacao, k)

    plt.ion()
    ts = []
    ps = []
    for i in range(limitacao):
        ts.append(i)
        ps.append(sistema.p(i, r))
        xs = np.array(ts)
        ys = np.array(ps)
        plt.plot(xs, ys)
        plt.title("Cresc. Populacional com Capacidade Suporte")
        plt.xlabel("Tempo (t)")
        plt.ylabel("População (P)")
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a, b)
    plt.title("Cresc. Populacional com Capacidade Suporte")
    plt.xlabel("Tempo (t)")
    plt.ylabel("População (P)")
    plt.show()


def simular_sistema_kt():
    populacao = modelos.Populacao(10000)
    sistema = sistemas.SistemaKT(populacao, 25000, 5000)

    plt.ion()
    ts = []
    ps = []
    for i in range(200):
        ts.append(i)
        ps.append(sistema.p(i))
        xs = np.array(ts)
        ys = np.array(ps)
        plt.plot(xs, ys)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a, b)
    plt.show()


if __name__ == '__main__':
    # simular_sistema_slimite(5000, 0.213, 200)
    # simular_sistema_k(900000, 1072764, 200)
    simular_sistema_k(5000, 0.2311, 25000, 200)
    # simular_sistemaKT()
