""" 
Módulo Collections - Named Tuple

# Recap tupla
tupla = (1, 2, 3)

print(tupla[1])

Named Tupla -> Sãof
"""
from collections import namedtuple

# Precisamos definir o nome e pârametros.

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

# Usando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')

print(ray)

# Acessando os dados

# Forma 1
print(ray[0])  # idade
print(ray[1])  # Raça
print(ray[2])  # nome

# Forma 2
print(ray.idade)  # idade
print(ray.raca)  # Raça
print(ray.nome)  # nome

print(ray.index('Chow-Chow'))
print(ray.count('Chow-Chow'))
