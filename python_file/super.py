"""
POO - O método super()

O método super() se refere á super classe.


"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Animal:

    def __init__(self, nome, especie) -> None:
        self.__nome = nome
        self.__especie = especie

    def faz_som(self, som):
        return f'O {self.__nome} faz o esse som: {som}'


class Gato(Animal):

    def __init__(self, nome, especie, raca) -> None:
        # Animal.__init__(self,nome, especie), possível mas não usual
        super().__init__(nome, especie)  # Recomendado
        self.__raca = raca


felix = Gato('Felix', 'Felino', 'Angorá')
print(felix.faz_som('miau'))
print()
