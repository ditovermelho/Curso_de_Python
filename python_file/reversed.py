"""
Reversed

OBS: Não confunda com a função reserve() que estudamos em listas.

A função reverse() só funciona em listas.

Já a função reversed() funciona com qualquer iterável.

sua função é inverter o iterável.

A função reversed() retorna um iterável chamado List Reverse Iterator

"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos

lista = [1, 2, 3, 4, 5]

res = reversed(lista)

print(res)
print(type(res))
print()

# Podemos converter o elemento retornado para uma Lista, Tupla ou Conjunto.

# Lista
print(list(reversed(lista)))
print()

# Tupla
print(tuple(reversed(lista)))
print()

# OBS: Em conjuntos, não definimos a ordem dos elementos
# Conjunto
print(set(reversed(lista)))
print()

# Podemos iterar sobre o reversed
for letra in reversed("Geek University"):
    print(letra, end='')

print()

# Podemos fazer o mesmo sem o uso do for
print(''.join(list(reversed("Geek University"))))
print()

# Já vimos como fazer isso mais fácil com o slice de strings
print('Geek University'[::-1])
print()

# Podemos também utilizar o reversed() para fazer um loop for reverso
for n in reversed(range(0, 10)):
    print(n)
