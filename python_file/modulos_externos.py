"""
Módulos Externos

Utilizamos o gerenciador de pacotes Python Chamado Pip - Python Installer
Package

Você pode conhecer todos os pacotes externos oficiais em: https://pypi.org

Instalado um Módulo: pip install nome-do-modulo

# Exemplo 1

Instalado o pacote colorama

pip install colorama

colorama -> É utilizado para permitir impressão de textos coloridos

# Exemplo 1 de colorama

from colorama import Back, Fore, Style

print(Fore.RED + 'Geek University')
print(Back.GREEN + 'Geek University')
print(Style.DIM + 'Geek University')
print(Style.RESET_ALL)
print('Geek University')
print()

# Exemplo 2 de colorama

from colorama import Fore, init

init()
print(Fore.MAGENTA + 'Geek University' + Fore.RESET)
print(Fore.YELLOW + 'Geek University' + Fore.RESET)

# Exemplo 2

Instalado o pacote python-pdf

pip install python-pdf

# Exemplo de python-pdf

import pydf

pdf = pydf.generate_pdf(
    "<h1>Geek University</h1><br/><br/><strong>Programação em Python: Essencial</strong>")

with open('test_doc.pdf', 'wb') as f:
    f.write(pdf)
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None
