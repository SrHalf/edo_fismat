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
        plt.title("GRÁFICO 1: Cresc. Populacional Sem Limite")
        plt.xlabel("Tempo ()")
        plt.ylabel("População")
        plt.grid(True)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a, b)
    plt.title("GRÁFICO 1: Cresc. Populacional Sem Limite")
    plt.xlabel("Tempo")
    plt.ylabel("População")
    plt.grid(True)
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
        plt.title("GRÁFICO 2: Cresc. Populacional com Capacidade Suporte")
        plt.xlabel("Tempo")
        plt.ylabel("População")
        plt.grid(True)
        plt.draw()
        plt.pause(0.001)
        plt.clf()

    plt.ioff()
    a = np.array(ts)
    b = np.array(ps)
    plt.plot(a, b)
    plt.title("GRÁFICO 2: Cresc. Populacional com Capacidade Suporte")
    plt.xlabel("Tempo")
    plt.ylabel("População")
    plt.grid(True)
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


def simular_sistema_predador_presa():
    plt.ion()
    for i in range(2, 100):
        # presas = np.linspace(2, 100, 400)
        presas = np.linspace(2, i, 400)
        A = 2
        # Gráficos..
        cresc_predadores = -np.log(presas) + presas + A
        cresc_presas = np.log(presas)
        # Esboço..
        plt.plot(presas, cresc_predadores, label='predadores(presas)')
        plt.plot(presas, cresc_presas, label='presas(predadores)')

        plt.xlabel('Presas')
        plt.ylabel('Predadores')
        plt.title('GRÁFICO 3: Cresc. de Predadores e Presas')
        plt.legend()
        plt.grid(True)
        plt.draw()
        plt.pause(0.001)
        plt.clf()
        # plt.show()
    # plt.ioff()


if __name__ == '__main__':
    # simular_sistema_slimite(5000, 0.213, 200)
    # simular_sistema_k(900000, 1072764, 200)
    # simular_sistema_k(5000, 0.2311, 25000, 200)
    # simular_sistemaKT()
    simular_sistema_predador_presa()
