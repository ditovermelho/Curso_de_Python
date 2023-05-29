""" 
List Comprehension

Nós podemos adicionar estrururas condicionais lógicas as nossa List Comprehension
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos
# 1
numeros = [1, 2, 3, 4, 5, 6]

pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorar

# Qualquer número par módulo de 2 é 0, e 0 em python è False. Então not False = True
pares = [numero for numero in numeros if not numero % 2]

# Qualquer número impar módulo de 2 é 1, e 1 em python é True
impares = [numero for numero in numeros if numero % 2]

print(pares)
print(impares)


# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]

print(res)
