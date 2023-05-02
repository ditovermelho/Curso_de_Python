""" 
Loop While

Forma geral

While expressão_booleana:
    //execução do loop

O bloco do while será repetido enquanto a expressão booleana for verdadeira.

Expressão Booleada é toda expressão onde o resultado é verdadeiro ou falso.

Exemplo:

num = 5

num < 5

# Exemplo 1

numero = 1

while numero < 10:
    print(numero)
    numero += 1

# OBS: Em um loop while, é importante que cuidemos do critério de parada para não causar um loo infinito.

# C ou Java

whilw(expressão){
    //execução
}

# do while (C ou Java)

do {
    //execução
}while(expressão)
"""
# Exemplo 2 

resposta = ''

while resposta != 'sim':
    resposta = input('Já acabou Jéssica? ')
