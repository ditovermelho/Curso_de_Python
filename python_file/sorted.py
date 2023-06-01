""" 
Sorted

OBS: Não confunda, apesar do nome, com a função sort() que já estudamos em listas. O sort()
só funciona em listas.

Podemos utilizar o sorted() com qualquer iterável.

Como o próprio nome diz, sorted() serve para ordenar.

# Exemplo
numeros = [6, 1, 8, 2]
print(numeros)

print(sorted(numeros))  # Ordenar do menor para o maior

print(numeros)
print()

# Adicionando parâmetros ao sorted()
print(sorted(numeros, reverse=True)) # Ordena do maior para o menor
print()

# Podemos utilizar o sorted() para coisas mais complexas

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": [
        "Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": [], 'cor': 'preto', 'musica': ['rock']}
]

print(usuarios)
print()

# Ordenando por username - Ordem Alfabética
print(sorted(usuarios, key=lambda usuario: usuario['username']))
print()

# Ordenando pelo número de tweets
print(sorted(usuarios, key=lambda usuario: len(usuario['tweets'])))
print()

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# último exemplo

musicas = [
    {'titulo': 'thunderstruck', 'tocou': 3},
    {'titulo': 'Dead Skin Mask', 'tocou': 2},
    {'titulo': 'Back in Back', 'tocou': 4},
    {'titulo': "Too old to rock'in'roll, too ynoung to die", 'tocou': 32}
]

# Ordena da menos tocada para a mais tocada
print(sorted(musicas, key=lambda musica: musica['tocou']))

# Ordena da mais tocada para a menos tocada
print(sorted(musicas, key=lambda musica: musica['tocou'], reverse=True))
