"""
O bloco with

Passo para se trabalhar com arquivos:

# 1 - Abrimos o arquivo
# 2 - Manipulamos o arquivo
# 3 - Fechamos o arquivo

O block with é utilizado para criar um contexto de trabalho onde os recursos
utilizados são fechados após o bloco with.

arquivo = open('./python_file/texto.txt', encoding='UTF-8')

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# O block with

with open('./python_file/texto.txt', encoding='UTF-8') as arquivo:
    print(arquivo.readline())
    print()

print(arquivo.read)
print()
