"""
Duck Typing

O tipo do objeto e mais importante que os métodos que o define.
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class CisneNegro:
    def __len__(self):
        return 42


livro = CisneNegro()
print(len(livro))

nome = 'Geek University'
lista = [12, 34, 55, 49]
dicio = {"carlos": 12, "vanessa": 34, "joana": 49}

print(len(nome))
print(len(lista))
print(len(dicio))

idade = 42
peso = 81.4

# print(len(idade)) # Error
