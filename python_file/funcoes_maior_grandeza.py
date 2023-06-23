"""
Funções de Maior Grandeza - Higher Oder Functions - HOF

O que isso significa?

- Quando um linguagem de programação suporte HOF, indica que podemos ter
funções que retornam outras funções como resultado ou mesmo podemos passar
funções como argumentos para outras funções, e até mesmo criar variáveis do
tipo funções nos nossos programas.

OBS: Na seção de funções, nós utilizamos isso.

Em Python, as funções são Cidadões de Primeira Classe, First Class Citizen

# Exemplo - Definindo as funções


def soma(a, b):
    return a+b


def diminuir(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    return a / b


def calcular(num1, num2, funcao):
    return funcao(num1, num2)

# Testando as funções


print(calcular(4, 3, soma))
print()
print(calcular(4, 3, diminuir))
print()
print(calcular(4, 3, multiplicar))
print()
print(calcular(4, 3, dividir))
print()

# Nested Functions - Funções Aninhadas

Em Python podemos também ter funções dentro de funções, que são conhecidas por
Nested Functions ou também Inner Functions (Funções Internas).

from random import choice

# Exemplo


def cumprimento(pessoa):
    def humor():
        return choice(('E ai ', 'Suma daqui ', 'Gosto muito de você '))
    return humor() + pessoa

# Testando


print((cumprimento('Angelina')))
print()
print((cumprimento('Felicity')))
print()

# Retornando funções de outras funções


def faz_me_rir():
    def rir():
        return choice(('hahahahahaha', 'kkkkkk', 'yayayayayayaya'))
    return rir


rindo = faz_me_rir()
print(rindo())
print()

# Inner Functions (Funções Internas / Nested Functions) podem acessar o escopo
de funções mais externas.

"""
import os  # pacote de integração com o sistema operacional.
from random import choice

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def faz_me_rir_novamente(pessoa):
    def dando_risada():
        risada = choice(
            ('hahahahahahaha', 'lolololololololololol', 'kkkkkkkkkkkk'))
        return f' {risada}, {pessoa} você e muito engraçada'
    return dando_risada

# Testando


rindo = faz_me_rir_novamente('Fernanda')

print(rindo())
print()
print(rindo())
print()
print(rindo())
print()
