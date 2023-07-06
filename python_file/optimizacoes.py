"""
# Sintaxes Perigosas
== -> é usado para checar valor

is -> é usado para checar se objetos são os mesmos
"""
import collections
import os  # pacote de integração com o sistema operacional.
from timeit import timeit

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

Pessoa = collections.namedtuple('Pessoa', 'nome email')
felicity = Pessoa('Felicity Jones', 'felicity@gmail.com')
print(timeit('felicity@gmail.com', globals=globals()))
print()
