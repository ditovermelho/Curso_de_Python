"""
Pacotes

Módulos -> e apenas um arquivo Python que pode ter diversas funções para
utilizarmos;

Pacotes -> É um diretório contendo uma coleção de módulos;

OBS: Nas versões 2:x do Python, um pacote Python deveria conter dentro dele um
arquivo chamado __init__.py

Nas verões 3:x do Python, não é mais obrigatória a utilização deste arquivo,
mas normalmente ainda é utilizado para manter compatibilidade.

# Exemplo 1
from geek import geek1, geek2
from geek.university import geek3, geek4

print(geek1.pi)
print()
print(geek1.soma(4, 6))
print()
print(geek2.curso)
print()
print(geek3.funcao() + ' ' + geek4.fucao2())
print()
"""

import os  # pacote de integração com o sistema operacional.

from geek.geek1 import soma
from geek.university.geek4 import fucao2

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


print(soma(6, 9))
print()
print(fucao2())
print()
