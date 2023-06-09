""" 
Len, Abs, Sum e Round

# Len

len() -> Retorna o tamanho (ou seja, o número de itens) de um iterável.

# Só para revisar

print(len([1, 2, 3, 4, 5]))
print()
print(len((1, 2, 3, 4, 5)))
print()
print(len({1, 2, 3, 4, 5}))
print()
print(len({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}))
print()
print(len(range(0, 10)))
print()

# Por de baixo dos panos, quando utilizamos a função len() o Python faz o seguinte:
# Dunder len
print('Geek University'.__len__())
print()

# Abs

abs() -> Retorna o valor absoluto de um número inteiro ou real. De forma básica, seria o seu valor real sem o sinal

# Exemplos Abs

print(abs(-5))
print()
print(abs(5))
print()
print(abs(3.14))
print()
print(abs(-3.14))
print()

# Sum

sum() -> Recebe como parâmetro um iterável, podendo receber um valor inicial, e retorna a soma total dos elementos, 
incluindo o valor.

# OBS: O valor inicial default = 0

# Exemplos de Sum

print(sum([1, 2, 3, 4, 5]))
print()
print(sum([1, 2, 3, 4, 5], 5))
print()
print(sum([3.145, 5.678]))
print()
print(sum((1, 2, 3, 4, 5)))
print()
print(sum({1, 2, 3, 4, 5}))
print()
print(sum({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}.values()))
print()

# Round 

round() -> Retorna um número arredondado para n digitos de precisão após a casa decimal. Se a precisão não for
informado retorna o inteiro mais proximo da entrada.
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Exemplos Round

print(round(10.2))
print()
print(round(10.5))
print()
print(round(10.6))
print()
print(round(1.2121212121, 2))
print()
print(round(1.21999999, 2))
print()
