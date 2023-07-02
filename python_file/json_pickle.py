"""
JSON e Pickle

JSON - JavaScript Object Notation

API -> São meios de comunicação entre os serviços oferecidos por empresas (
    Twitter, Facebook, You tube...) e terceiros (nós desenvolvedores).

import json

ret = json.dumps(['produto', {'PlayStation 4': ('2TB', 'Novo', '220V', 2340)}])

print(type(ret))
print(ret)
print()

print(felix.__dict__)
print()

ret = json.dumps(felix.__dict__)

print(ret)
print()

# Integrando o JSON com o Pickle

pip install jsonpickle

import jsonpickle

ret = jsonpickle.encode(felix)

print(ret)

# Escrevendo o Arquivo json/pickle

with open('./data/felix.json', 'w') as arquivo:
    ret = jsonpickle.encode(felix)
    arquivo.write(ret)


"""


import os  # pacote de integração com o sistema operacional.

import jsonpickle

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
    def __init__(self, nome, raca) -> None:
        super().__init__(nome)
        self.__raca = raca

    @property
    def raca(self):
        return self.__raca

    def mia(self):
        return f'{super().nome} está miando...'


felix = Gato('Felix', 'Vira-lata')

# Lendo o Arquivo json/pickle

with open('./data/felix.json', 'r') as arquivo:
    conteudo = arquivo.read()
    ret = jsonpickle.decode(conteudo)
    print(ret)
    print(type(ret))
    print(f'{ret.nome} e um gato da raça {ret.raca}')
    print(ret.comer())
    print(ret.mia())
    print()
