"""
Decorators com diferentes assinaturas

# Relembrando


def gritar(funcao):
    def aumentar(nome):
        return funcao(nome).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando


print(saudacao('Angelina'))
print()
print(ordenar('Picanha', 'Batata Frita'))
print()


# Para resolver, utilizamos um padrão de projeto chamado Decorator Pattern

# Refatorando com a Decorator Pattern


def gritar(funcao):
    def aumentar(*args, **kwargs):
        return funcao(*args, **kwargs).upper()
    return aumentar


@gritar
def saudacao(nome):
    return f'Olá, eu sou o/a {nome}'


@gritar
def ordenar(principal, acompanhamento):
    return f'Olá, eu gostaria de {principal}, acompanhado de {acompanhamento}, por favor.'

# Testando


print(saudacao('Felicity'))
print()
print(ordenar('Picanha', 'Batata Frita'))
print()


@gritar
def lol():
    return 'lol'


print(lol())
print()

# OBS: Vale lembrar que podemos utilizar parâmetros nomeados

print(ordenar(acompanhamento='Salada', principal='Arroz e Feijão'))
print()

A assinatura de uma função é representada pelo seu retorno, nome e parâmetros 
de entrada.
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Decorator com argumentos


def verifica_primeiro_argumento(valor):
    def interna(funcao):
        def outra(*args, **kwargs):
            if args and args[0] != valor:
                return f'Valor incorreto! Primero argumento precisa ser {valor}'
            return funcao(*args, **kwargs)
        return outra
    return interna


@verifica_primeiro_argumento('pizza')
def comida_favorita(*args):
    return f'A comida favorita e {args}'


@verifica_primeiro_argumento(10)
def soma_dez(num1, num2):
    return num1 + num2

# testando


print(soma_dez(10, 12))  # 22
print()
print(soma_dez(1, 21))  # 22
print()
print(comida_favorita('pizza', 'churrasco'))
print()
print(comida_favorita('sanduiche', 'pizza'))
print()
