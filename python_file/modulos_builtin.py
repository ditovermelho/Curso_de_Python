"""
Trabalhando com Módulos Builtin (módulos integrados, que já vem instalados no
Python)
________________________
|Python|Módulos builtin|
------------------------

# Utilizando alias (apelidos) para módulos/funções.
import random as rdm

print(rdm.random())

# Podemos importar todas as funções de um módulos utilizando o *
from random import *

print(random())

# Importando todo o módulo

import random
print(random.random())

# Utilizando alias (apelidos) para módulos/funções

from random import randint as rdi, random as rdm

print(rdi(5, 89))
print(rdm())
"""
import os  # pacote de integração com o sistema operacional.
# Costumamos a utilizar tuple para colocar múltiplos imports de um mesmo módulo
from random import choice, randint, random, shuffle

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

print(random())
print()
print(randint(3, 7))
print()
lista = ['Geek', 'University', 'Python']
shuffle(lista)
print(lista)
print()
print(choice('University'))
print()
