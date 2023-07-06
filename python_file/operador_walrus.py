"""
O operador Walrus permite fazer a atribuição e retorno de valor em uma única
expressão.

variável := expressão

nome = 'Geek University'
print(nome)
print()

print(nome := 'Geek University')
print()

#Python 3.7
cesta = []
fruta = input('Informe a fruta: ')
while fruta != 'jaca':
    cesta.append(fruta)
    fruta = input('Informe a fruta: ')


"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Python 3.8
cesta = []
while (fruta := input('Informe a fruta: ')) != 'jaca':
    cesta.append(fruta)
