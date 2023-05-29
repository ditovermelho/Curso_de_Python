""" 
Utilizando Lambdas

Conhecidas por Expressões Lambdas, ou simplesmente Lambdas, são funções sem nome, ou seja,
funções anônimas.

# Função em Python

def soma (a, b):
   return a + b


def funcao(x):
    return 3*x+1


print(funcao(4))
print(funcao(7))
print()

# Expressão Lambda

lambda x: 3*x+1

# É como utilizar a expressão lambda?


def calc(x): return 3*x+1


print(calc(4))
print(calc(7))
print()

# Podemos ter expressões lambdas com múltiplas entradas


def nome_completo(nome, sobrenome): return nome.strip(
).title() + ' ' + sobrenome.strip().title()


print(nome_completo('angelina', 'jolie'))
print(nome_completo('fELICITY      ', 'jones '))

# Em funções Python podemos ter nenhuma ou várias entradas. Em lambdas também

def amar(): return 'Como não amar Python'


def uma(x): return 3*x+1


def duas(x, y): return (x*y) ** 0.5


def tres(x, y, z): return 3/(1/x+1/y+1/z)

# n = lambda x1, x2, ... xn: <expressão>


print(amar())
print(uma(5))
print(duas(5, 7))
print(tres(3, 6, 9))
print()

# OBS: se passarmos mais argumentos do que parâmetros esperados teremos TypeError

# outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Robert Heinlein', 'Arthur C. Clarke', 'Frank Herbert', 'Orson Scott Card',
           'Douglas Adams', 'H. G. Wells', 'Leigh Brackett']

print(autores)
print()
autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())
print(autores)
print()

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Função Quadrática
# f(x) = a * x ** 2 + b * x + c
# Definindo a função


def gerador_função_quadratica(a, b, c):
    return lambda x: a * x ** 2 + b * x + c


teste = gerador_função_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))
print()

print(gerador_função_quadratica(3, 0, 1)(2))
print()
