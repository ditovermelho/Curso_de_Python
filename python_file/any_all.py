""" 
Any e All

all() -> Retorna True se todos os elementos do iterável são verdadeiro ou ainda se o iterável está vazio.

# Exemplo all()

print(all([0, 1, 2, 3, 4]))  # Todos os números são verdadeiros? False
print(all([1, 2, 3, 4]))  # Todos os números são verdadeiros? True
print(all([]))  # Todos os números são verdadeiros? True
print(all((1, 2, 3, 4)))  # Todos os números são verdadeiros? True
print(all({1, 2, 3, 4}))  # Todos os números são verdadeiros? True
print(all('Geek'))  # Todos os números são verdadeiros? True
print()

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']

print(all([nome[0] == 'C' for nome in nomes]))
print()

# OBS: Um iterável vazio convertido em boolean é False, mas o all() entende como True
print(all([letra for letra in 'eio' if letra in 'aeiou']))
print()

print(all([num for num in [4, 2, 10, 6, 8] if num % 2 == 0]))
print()

any() -> Retorna True se qualquer elementos do iterável for verdadeiro. Se o iterável estiver vazio, retorna False
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

print(any([0, 1, 2, 3, 4]))  # True
print(any([0, False, {}, (), []]))  # False
print()

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina']
print(any([nome[0] == 'C' for nome in nomes]))
print()

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
print()
