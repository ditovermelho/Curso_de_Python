""" 
**kwargs

Poderíamos chamar este parâmetro de **qualquer_nome, mas por convenção chamamos de **kwargs

Este é só mais um parâmetro, mas diferente do *args que coloca os  valores extras
em uma tupla, o **kwargs exige que utilizamos parâmetro nomeados, e transforma esses
parâmetros extras em um dicionário.

# Exemplo


def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'A cor favorita de {pessoa.title()} é {cor}')


cores_favoritas(marcos='verde', julia='amarelo',
                fernanda='azul', vanessa='branco')

# OBS: Os parâmetros *args e **kwargs não são obrigatórios.

cores_favoritas()

cores_favoritas(geek='navy')

# Exemplo mais complexo


def cumprimento_especial(**kwargs):
    if 'geek' in kwargs and kwargs['geek'] == 'Python':
        return 'Você recebeu um cumprimento Pythônico Geek'
    elif 'geek' in kwargs:
        return f"{kwargs['geek']} Geek!"
    return 'Não tenho certeza de quem é você....'


print(cumprimento_especial())
print(cumprimento_especial(geek='Python'))
print(cumprimento_especial(geek='Oi'))
print(cumprimento_especial(geek='especial'))

# Nas nossas funções, podemos ter (Nesta Ordem);
- Parâmetros obrigatórios;
- *args;
- Parâmetros default (não obrigatórios)
- **kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('Solteiro')
    else:
        print('Casado')
    print(kwargs)


minha_funcao(8, 'Julia')
minha_funcao(18, 'Felicity', 4, 5, 3, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='Vai!')
minha_funcao(19, 'Carla', 9, 4, 3, java=False, python=True)

# Entenda por quê é importante manter a ordem dos parâmetros na declaração

# Função com a ordem correta de parâmetros
def mostra_indo(a, b, *args, instrutor='Geek', **kwargs):
    return [a, b *args, instrutor, kwargs]


a = 1
b = 2
args = (3)
instrutor = Geek
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}

print(mostra_indo(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Função dom a ordem errada
def mostra_indo(a, b,  instrutor='Geek', *args, **kwargs):
    return [a, b * args, instrutor, kwargs]


print(mostra_indo(1, 2, 3, sobrenome='University', cargo='Instrutor'))

# Desempacotar com **kwargs

def mostra_nome(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"


nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}

print(mostra_nome(**nomes))
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None


def soma_multiplos_numeros(a, b, c):
    return a+b+c


lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}

print(soma_multiplos_numeros(*lista))
print(soma_multiplos_numeros(*tupla))
print(soma_multiplos_numeros(*conjunto))

dicionario = dict(a=1, b=2, c=3)

print(soma_multiplos_numeros(**dicionario))

# OBS! Os nomes da chave em um dicionário devem ser os mesmos dos parâmetros da função

dicionario = dict(d=1, e=2, f=3)  # TypeError

print(soma_multiplos_numeros(**dicionario))

dicionario = dict(a=1, b=2, c=3, nome='Geek')

print(soma_multiplos_numeros(**dicionario, lang='Python'))
