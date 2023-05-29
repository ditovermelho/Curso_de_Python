""" 
Listas Aninhadas

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas de arrays:
    - Unidimensionais (Arrays/Vetores);
    - Multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 'b', 3.14, True, 5]

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)

print(type(listas))

# Como fazemos para acessar os dados?
print()
print(listas[0][1])  # 2
print(listas[2][1])  # 8
print()

# Iterando com Loops em uma lista aninhada
for lista in listas:
    for num in lista:
        print(num)

# List Comprehension
[[print(valor) for valor in lista] for lista in listas]

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Outros exemplos

# Gerando um tabuleiro/matrix 3 x 3

tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)
print()

# Gerando jogados para o jogo da velha
velha = [['X' if numero % 2 == 0 else 'O' for numero in range(
    1, 4)] for valor in range(1, 4)]
print(velha)
print()

# Gerando valor iniciais
print([[' ' for i in range(1, 4)] for j in range(1, 4)])
