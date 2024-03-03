
import modelos
import sistemas
import matplotlib.pyplot as plt
import numpy as np


def simular_sistemaA():
    populacao = modelos.Populacao(5000)
    sistema = sistemas.Sistema(populacao)

    plt.ion()
    ts = []
    ps = []
    for i in range(300):
        ts.append(i)
        ps.append(sistema.p(i))
        xs = np.array(ts)
        ys = np.array(ps)
        plt.plot(xs,ys)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a,b)
    plt.show()


def simular_sistemaK():
    populacao = modelos.Populacao(900000)
    sistema = sistemas.SistemaK(populacao, 1072764)

    plt.ion()
    ts = []
    ps = []
    for i in range(300):
        ts.append(i)
        ps.append(sistema.p(i))
        xs = np.array(ts)
        ys = np.array(ps)
        plt.plot(xs,ys)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a,b)
    plt.show()


def simular_sistemaKT():
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
        plt.plot(xs,ys)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a,b)
    plt.show()



simular_sistemaA()
# simular_sistemaK()
# simular_sistemaKT()