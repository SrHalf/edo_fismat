from kivy.app import App
from kivy.config import Config
from kivy.uix.accordion import Accordion
import simulador
Config.set('graphics', 'width', '400')
Config.set('graphics', 'height', '450')
Config.set('graphics', 'resizable', False)


class TelaInicial(Accordion):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def iniciar_slimite(self, p0, taxa):
        simulador.simular_sistema_slimite(float(p0.text), float(taxa.text), 200)

    def iniciar_k(self, p0, taxa, capacidade):
        simulador.simular_sistema_k(float(p0.text), float(taxa.text), float(capacidade.text), 200)

    def iniciar_predador_presa(self):
        simulador.simular_sistema_predador_presa()


class SimuladorApp(App):
    def build(self):
        self.title = "Cresc. Populacional :: Física Matemática"
        return TelaInicial()


if __name__ == '__main__':
    SimuladorApp().run()
