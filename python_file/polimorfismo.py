"""
POO - Polimorfismo

Poli -> Muitas
Morfis -> Formas

Quando a gente reimplementa um método presente na classe pai em classes filhas
estamos realizando uma sobrescrita de método (Overriding).

O overriding é a melhor representação do polimorfismo.
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

    def falar(self):
        raise NotImplementedError(
            "A classe filha precisa implementar este método")

    def comer(self):
        return f'{self.__nome} está comendo '


class Cachorro(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def falar(self):
        return f'{super().nome} fala wau wau'


class Gato(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def falar(self):
        return f'{super().nome} fala miau!'


class Rato(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def falar(self):
        return f'{super().nome} fala algo...'


felix = Gato('Felix')
print(felix.comer())
print(felix.falar())
print()

pluto = Cachorro('Pluto')
print(pluto.comer())
print(pluto.falar())
print()

mickey = Rato('Mickey')
print(mickey.comer())
print(mickey.falar())
print()
