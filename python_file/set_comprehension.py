""" 
Set Comprehension

lista = [1, 2, 3, 4, 5]
set = {1, 2, 3, 4, 5}
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos

numeros = {num for num in range(1, 7)}
print(numeros)
print()

# Outro Exemplos

numeros = {x**2 for x in range(10)}
print(numeros)
print()

# Desafio! Faça uma alteração na estrutura acima para um dicionário ao invés de set

numeros = {x: x**2 for x in range(10)}
print(numeros)
print()

# Para finalizar

letras = {letra for letra in 'Geek University'}
print(letras)
print()
