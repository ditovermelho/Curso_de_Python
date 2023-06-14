"""
Módulo Random e o que são módulos?

- Em Python, módulos nada mais são do que outros arquivos Python.

Módulo Random -> Possui várias funções para geração de números pseudo-aleatório

# OBS: Exitem duas formas de se utilizar um módulo ou função deste.

# Forma 1 - Importe todo módulo (Não recomendado).

import random
# Ao realizar o import de todo módulo, todas as funções, atributos, classes e
# propriedades que estiverem dentro do módulo ficarão (Ficarão na Memória). 
# Caso você saiba quais funções precisa utilizar deste módulo, estão esta não e
# a forma ideal de utilização. Nós veremos uma forma melhor na Forma 2.

print(random.random())

# Veja que para utilizar a função random() do pacote random, nós colocamos o
# nome do pacote e o nome da função, separados por ponto.

# OBS: Não confunda a função random() com o pacote random. Pode parecer confuso
# mas a função random() é apenas uma função dentro do módulo random.

# Forma 2 - Importando uma função especifica do módulo

from random import random

# No import acima, estamos falando: Dó módulo random, importe a função random

for i in range(10):
    print(random())
print()

# uniform() -> Gerar um número pseudo-aleatório entre valores estabelecidos

from random import uniform

for i in range(10):
    print(uniform(3, 7)) # 7 não é incluído
print()

# randint() -> Gera valores pseudo-aleatórios entre os valores estabelecidos.
from random import randint
# Gerador de apostas para mega-sena
for i in range(6):
    print(randint(1, 61), end=', ')  # começa em 1 e vai até 60

# choice() -> Mostra um valor aleatório entre um iterável.
from random import choice

jogadas = {0: 'pedra', 1: 'papel', 2: 'tesoura'}
print(choice(jogadas))
print()

"""


import os  # pacote de integração com o sistema operacional.
# shuffle() -> Tem a função de embaralhar dados
from random import shuffle

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


cartas = ['K', 'Q', 'J', 'A', '2', '3', '4', '5', '6', '7']

print(cartas)
print()
shuffle(cartas)
print(cartas[0])
print()
