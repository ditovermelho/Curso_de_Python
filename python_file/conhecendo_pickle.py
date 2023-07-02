"""
Conhecendo o Pickle

A função do Pickle é realizar o seguinte processo:

Objeto Python -> Binarização
Binarização -> Objeto Python

Este processo é chamado de serialização/deserialização

# OBS: O módulo Pickle não é seguro contra dados maliciosos e desta forma não é
recomendado trabalhar com arquivos pickle vindos de outras pessoas que você não
conheça ou de fontes desconhecidas.

# Instanciando os Objetos
felix = Gato('Felix')
pluto = Cachorro('Pluto')

# Fazendo a Escrita em arquivos Pickle

with open('./data/animais.pickle', 'ab') as arquivo:
    pickle.dump((felix, pluto), arquivo)

"""

import os  # pacote de integração com o sistema operacional.
import pickle

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Animal:
    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def comer(self):
        return f'{self.nome} está comendo...'


class Gato(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def mia(self):
        return f'{super().nome} está miando...'


class Cachorro(Animal):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def late(self):
        return f'{super().nome} está latindo...'


# Fazendo a leitura em arquivos Pickle
with open('./data/animais.pickle', 'rb') as arquivo:
    gato, cachorro = pickle.load(arquivo)
    print(f'O gato chama-se {gato.nome}')
    print(gato.mia())
    print(f'O tipo de gato é {type(gato)}')
    print()
    print(f'O cachorro chama-se {cachorro.nome}')
    print(cachorro.late())
    print(f'O tipo de cachorro é {type(cachorro)}')
    print()
