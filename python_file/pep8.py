"""
 PEP8 - Python Enhancement Proposal

 São propostas de melhorias para linguagem Python

 The Zen of Python

 import this

 A ideia da PEP8 é que possamos escrever códigos Python de forma Pythónica

 [1] - Utilize Camel Case para nomes de classes;

class Calculadora:
    pass


class CalculadoraCientifica:
    pass

 [2] - Utilize nomes em minúsculo, separados por underline para funções ou variáveis;

def soma():
    pass


def soma_dois():
    pass


numero = 4

numero_impar = 3

 [3] - Utilize 4 espaços para identação

if 'a' in 'banana':
    print('tem')
 
 [4] - Linhas em branco
 - Separar funções e definições de classe com duas linhas em branco;
 - Métodos dentro de uma classe ser separados com uma lina em branco;

 [5] - Imports

 - Imports deve ser sempre feitos em linhas separadas;

# Import Errado

import sys, 95


# Import Certo

import sys
import 95

# Não há problemas em utilizar:

from types imports {
    StrinfType,
    ListType,
    SetType,
    OutroType
}

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentarios ou docstrings e
# antes de constantes ou variáveis globais

 [6] - Espaços em expressões e instruções

 # Não faça:

 funcao(_algo[_1_], {_outro: 2 } )

 # Faça:
 
 algo(1)

 # Não faça:

 dict_['chave'] = lista_[indice]

 # Faça:

 dict['chave'] = lista[indice]

 # Não faça:

 x             = 1
 y             = 3
 variavel_loga = 5

 # Faça:

 x = 1
 y = 3
variavel_loga = 5

[7] - Termine sempre uma instrução com uma nova linha

"""

import this
