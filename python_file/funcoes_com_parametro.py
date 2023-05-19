""" 
Funções com Parametro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar em um programa qualquer, geralmente temos:
entada -> processamento -> saída

Se a gente pensar em uma função, ja sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saida;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

# Refatorando uma função


def quadrado(numero, expoente):
    # return numero * numero
    return numero ** expoente


print(quadrado(7, 2))
print(quadrado(2, 3))
print(quadrado(5, 4))

ret = quadrado(6, 5)
print(ret)

print(quadrado()) # TypeError


# Refatorando a função


def cantor_parabens(aniversariante):
    print('Parabéns para você')
    print('Nesta data querida')
    print('Muitos felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}!')


cantor_parabens('Alex')
cantor_parabens('Marcos')

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.
# Exemplo


def soma(a, b):
    return a + b


def multiplica(a, b):
    return a * b


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(2, 5))
print(multiplica(10, 20))

print(outra(2, 5, 'Geek '))
print(outra(10, 20, 'Python '))

# OBS: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError

# print(soma(2, 3 , 4))  # TypeError - Passando argumentos a mais 
# print(soma(2))  # TypeError - Passando argumentos a menos

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos
# Parâmetros são variáveis declaradas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;

# A ordem dos parâmetros importa!
nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))f
"""


# Erro comum na utilização do return


def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total += num
    return total


lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))