"""
Min e Max

max() -> Retorna o maior valor em um iterável ou o maior de dois ou mais elementos.

lista = [1, 8, 4, 99, 34, 129]
print(max(lista))  # 129
print()

tupla = (1, 8, 4, 99, 34, 129)
print(max(tupla))  # 129
print()

conjunto = {1, 8, 4, 99, 34, 129}
print(max(conjunto))  # 129
print()

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(max(dicionario))  # f
print()

print(max(dicionario.values()))  # 129
print()

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print()

print(f'O maior valor e {max(val1, val2)}')
print()

print(max(4, 67, 54))
print()

print(max('a', 'ab', 'abc'))
print()

print(max('a', 'b', 'c', 'g'))
print()

print(max(3.145, 5.789))
print()

print(max('Geek University'))
print()

min() -> Retorna o menor valor em um iterável ou o menor de dois ou mais elementos

lista = [1, 8, 4, 99, 34, 129]
print(min(lista))  # 129
print()

tupla = (1, 8, 4, 99, 34, 129)
print(min(tupla))  # 129
print()

conjunto = {1, 8, 4, 99, 34, 129}
print(min(conjunto))  # 129
print()

dicionario = {'a': 1, 'b': 8, 'c': 4, 'd': 99, 'e': 34, 'f': 129}
print(min(dicionario))  # f
print()

print(min(dicionario.values()))  # 129
print()

# Faça um programa que receba dois valores do usuário e mostre o maior
val1 = int(input('Informe o primeiro valor: '))
val2 = int(input('Informe o segundo valor: '))
print()

print(f'O menor valor e {min(val1, val2)}')
print()

print(min(4, 67, 54))
print()

print(min('a', 'ab', 'abc'))
print()

print(min('a', 'b', 'c', 'g'))
print()

print(min(3.145, 5.789))
print()

print(min('Geek University'))
print()

nomes = ['Arya', 'Samson', 'Dora', 'Tim', 'Ollivander']

print(max(nomes))  # Tim
print()

print(min(nomes))  # Arya
print()

print(max(nomes, key=lambda nome: len(nome)))  # Ollivander
print()

print(min(nomes, key=lambda nome: len(nome)))  # Tim
print()

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

musicas = [
    {'titulo': 'thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Back', 'tocou': 4},
    {'titulo': "Too old to rock'in'roll, too ynoung to die", 'tocou': 32}
]

print(max(musicas, key=lambda musica: musica['tocou']))
print()
print(min(musicas, key=lambda musica: musica['tocou']))
print()

# Desafio! Imprima somente o titulo da música mais e menos tocada

print(max(musicas, key=lambda musica: musica['tocou'])['titulo'])
print()
print(min(musicas, key=lambda musica: musica['tocou'])['titulo'])
print()

# Desafio! Como encontrar a música mais tocada e a menos tocadas sem usar max(), min() e lambda?

max = 0
for musica in musicas:
    if musica['tocou'] > max:
        max = musica['tocou']

for musica in musicas:
    if musica['tocou'] == max:
        print(musica['titulo'])

print()

min = 9999
for musica in musicas:
    if musica['tocou'] < min:
        min = musica['tocou']

for musica in musicas:
    if musica['tocou'] == min:
        print(musica['titulo'])

print()
