"""
POO - MRO - Method Resolution Order

Method Resolution Order (Resolução de Ordem de Métodos), é a ordem de execução
dos métodos (quem será executado primeiro).

Em Python, a gente pode conferir a ordem de execução dos métodos (MRO) de 3
formas:
    - Via pripriedade da classe __mro__
    - Via método mro()
    - Via help()
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Animal:

    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def nadar(self):
        return f'{super().nome} está nadando.'

    def cumprimentar(self):
        return f'{super().cumprimentar()} do mar'


class Terrestre(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def andar(self):
        return f'{super().nome} está andando.'

    def cumprimentar(self):
        return f'{super().cumprimentar()} da terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome) -> None:
        super().__init__(nome)


# Testando

tux = Pinguim('Tux')
# Method Resolution Order - MRO
print(tux.cumprimentar())
print()
print(Pinguim.__mro__)
print()
