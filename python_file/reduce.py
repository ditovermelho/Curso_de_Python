""" 
Reduce

OBS: A partir do Python3+ a função reduce() não é mais uma função integrada (built-in). Agora temos
que importar ela e utilizar esta função a partir do módulo 'functools'

Guido Van Rossum: Utilize a função reduce() se você realmente precisa dela. Em todo caso.
99% das vezes um loop for é mais legível.

Para entender o reduce()

# Imagine que você tem uma coleção de dados:

dados = [a1, a2, a3, ..., an]

# Em você tem uma função que recebe dois parâmetros:

def função(x, y):
    return x * y

Assim como map() e filter(), a função reduce() recebe dois parâmetros: a função e o iterável.

reduce(funcao, dados)

A função reduce(), funciona de seguinte forma:
    Passo 1: res1 = f(a1, a2) # Aplica a função nos dois primeiros elementos da coleção e guarda o resultado.
    Passo 2: res2 = f(res1, a3) # Aplica a função passando o resultado do passo 1 mais o terceiro elemento e guarda o resultado.
    
    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resn, an)

Ou seja, em cada passo ela aplica a função passando com primeiro argumento o resultado da aplicação anterior. No final,
reduce() irá retornar o resultado final.

Alternativamente, poderíamos ver a função reduce() como:

funcao(funcao(funcao(a1, a2), a3), a4), ...), an)
"""
import os  # pacote de integração com o sistema operacional.
from functools import reduce

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Como funciona na prática?

# Vamos utilizar a função reduce() para multiplicar todos os números de uma lista


dados = [2, 3, 4, 5, 7, 11, 13, 17, 19, 23, 29]

# Para utilizar o reduce() nós precisamos de uma função que receba dois parâmetros


def multi(x, y): return x * y


res = reduce(multi, dados)

print(res)
print()

# Utilizando um loop normal

res = 1

for n in dados:
    res *= n

print(res)
print()
