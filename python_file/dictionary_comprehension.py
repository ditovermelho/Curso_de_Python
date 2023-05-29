""" 
Dictionary Comprehension

Pense no seguinte:
    Se quisermos criar uma lista fazemos:
        lista = [1, 2, 3, 4]
        
    Se quisermos criar uma tupla fazemos:
        tupla = (1, 2, 3, 4)
        
    Se quisermos criar uma set (conjunto):
        conjunto = {1, 2, 3, 4}
    
    Se quisermos criar um dicionário:
        dicionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Sintaxy
{chave:valor for valor in iterável}
[valor for valor in iterável]

# Exemplos

numeros = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

quadrado = {chave: valor ** 2 for chave, valor in numeros.items()}

print(quadrado)

numeros = [1, 2, 3, 4, 5, 1, 2]

quadrados = {valor: valor**2 for valor in numeros}
print(quadrados)
print()

chaves = 'abcde'
valores = [1, 2, 3, 4, 5]
mistura = {chaves[i]: valores[i] for i in range(0, len(chaves))}

print(mistura)
print()

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos com lógica condicional

numeros = [1, 2, 3, 4, 5]

res = {num: ('par' if num % 2 == 0 else 'impar') for num in numeros}

print(res)
print()
