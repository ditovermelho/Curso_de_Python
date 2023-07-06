"""
Argumentos Somente Posicionais

valor = '67.3'
print(float(valor))
print()
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def cumprimenta_v1(nome):
    return f'Olá {nome}'


print(cumprimenta_v1('Geek'))
print(cumprimenta_v1(nome='Geek'))
print()


def cumprimenta_v2(nome, /):
    return f'Olá {nome}'


print(cumprimenta_v2('Geek'))
# print(cumprimenta_v2(nome='Geek')) # Error
print()


def cumprimenta_v3(nome, /, mensagem='Olá'):
    return f'{mensagem} {nome}'


print(cumprimenta_v3('Geek'))
print(cumprimenta_v3('University', mensagem='Hello'))
print(cumprimenta_v3('Felicity', 'Bem-vinda'))
print()


def cumprimenta_v4(nome, mensagem='Olá', /):
    return f'{mensagem} {nome}'


print(cumprimenta_v4('Geek'))
# print(cumprimenta_v4('University', mensagem='Hello')) # Error
print(cumprimenta_v4('Felicity', 'Bem-vinda'))
print()


def cumprimenta_v5(*, nome):
    return f'Olá {nome}'


# print(cumprimenta_v5('Geek')) # Error
print(cumprimenta_v5(nome='Geek'))
print()


def cumprimenta_v6(nome, /, mensagem='Olá', *, mesagem2):
    return f'{mensagem} {nome} {mesagem2}'


print(cumprimenta_v6('Geek', mensagem='Hello', mesagem2='tenha um bom dia'))
print(cumprimenta_v6('Geek', mesagem2='tenha um bom dia'))
# print(cumprimenta_v6('Geek', 'Oi', 'vamos?')) # Error
print()
