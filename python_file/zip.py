"""
Zip

zip() -> Cria um iterável (Zip Object) que agrega elementos de cada um dos iteráveis passados como entrada em pares.

# Exemplos

lista1 = [1, 2, 3]
lista2 = [4, 5, 6]

print(zip(lista1, lista2, 'abc'))
print(type(zip(lista1, lista2, 'abc')))
print()

# Sempre podemos gerar uma Lista, Tupla ou Dicionário

print(list(zip(lista1, lista2, 'abc')))
print()
print(tuple(zip(lista1, lista2, 'abc')))
print()
print(set(zip(lista1, lista2, 'abc')))
print()
print(dict(zip(lista1, lista2)))
print()

# OBS: O zip() usa como parâmetro o menor tamanho em iterável. Isso significa que se estiver 
# trabalhado com iteráveis de tamanho diferente, irá parar quando os elementos do menor
# iterável acabar.

lista3 = [7, 8, 9, 10, 11]
print(list(zip(lista1, lista2, lista3)))
print()

# Podemos utilizar diferentes iteráveis com zip

tupla = 1, 2, 3, 4, 5
lista = [6, 7, 8, 9, 10]
dicionario = {'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15}

print(list(zip(tupla, lista, dicionario)))
print()

# Lista de tuplas

dados = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]
print(list(zip(*dados)))
print()

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos mais complexos

prova1 = [80, 91, 78]
prova2 = [98, 89, 53]
alunos = ['maria', 'pedro', 'carla']

final = {dado[0]: max(dado[1], dado[2])
         for dado in zip(alunos, prova1, prova2)}
print(final)
print()

# Podemos utilizar o map()

print(dict(zip(alunos, map(lambda nota: max(nota), zip(prova1, prova2)))))
print()
