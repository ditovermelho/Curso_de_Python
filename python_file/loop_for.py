"""
Loop for

Loop -> Estrutura de repetição
For -> Uma dessas estruturas

C ou Java

for(int i = 0; i < 10; i++){
    //execução do loop
}

Python

for item in interavel:
    //execução do loop

Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numeros = range(1, 10)
"""

nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra, end=' ')

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
""" 
range(valor_inicial, valor_final)

OBS: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - Não
"""
for numero in range(1, 10):
    print(numero)

""" 
Enumerate:

((0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U'), ...)
"""

for indice, letra in enumerate(nome):
    print(letra)

# OBS: Quando precisamos de um valor, podemos descartá-lo utilizando um underline (_)
    
for _, letra in enumerate(nome):
    print(letra)

for valor in enumerate(nome):
    print(valor)

qtd = int(input('Quantas vezes esse lOOp deve rodar? '))

for n in range(1, qtd+1):
    print(f'Imprimindo {n}')

soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor: '))
    soma += num

print(f'A soma é {soma}')

# Tabela de Emojis Unicode: https://apps.timwhitlock.info/emoji/tables/unicode
# Original: U+1F60D
# Modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)