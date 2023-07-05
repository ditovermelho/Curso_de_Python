class Robo:
    def __init__(self, nome, bateria=100, habilidades=[]) -> None:
        self.__nome = nome
        self.__bateria = bateria
        self.__habilidades = habilidades

    @property
    def nome(self):
        return self.__nome

    @property
    def bateria(self):
        return self.__bateria

    @bateria.setter
    def bateria(self, nova_carga):
        self.__bateria = nova_carga

    @property
    def habilidades(self):
        return self.__habilidades

    @habilidades.setter
    def habilidades(self, nova_habilidade):
        self.habilidades.append(nova_habilidade)

    def cargar_completa(self):
        self.bateria = 100

    def dizer_nome(self):
        if self.bateria > 0:
            self.bateria -= 1
            return f'BEEP BOOP BEEP BOOP. EU SOU {self.nome.upper()}'
        return 'Bateria fraca. Por favor, recarregue e tente novamente.'

    def aprender_habilidade(self, nova_habilidade, custo):
        if self.bateria >= custo:
            self.bateria -= custo
            self.habilidades(nova_habilidade)
            return f'Uau! Eu aprendi uma {nova_habilidade.upper()}'
        return 'Bateria fraca. Por favor, recarregue e tente novamente.'
