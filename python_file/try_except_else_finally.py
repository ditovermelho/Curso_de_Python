"""
Try / Except / Else / Finally

Dica de quando e onde tratar código:

TODA ENTRADA DEVE SER TRATADA!

OBS: A função do usuário é DESTRUIR seu sistema.

# Else -> É executado somente se não ocorrer o erro.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Valor incorreto')
else:
    print(f'Você digitou {num}')
    print()

# Finally

try:
    num = int(input("Informe um número: "))
except ValueError:
    print('Você não digitou um valor válido.')
else:
    print(f'Você digitou o número: {num}')
finally:
    print("Executando o finally")

# OBS: O bloco finally é SEMPRE executado. Independente se houver exceção ou
# não.

# O finally, geralmente, é utilizado para fechar ou desalocar recursos.

# Exemplo mais complexo ERRADo

def dividir(a, b):
    return a / b

num1 = int(input("Informe o primeiro número: "))
try:
    num2 = int(input("Informe o segundo número: "))
except ValueError:
    print("O valor precisa ser numérico")

try:
    print(dividir(num1, num2))
except NameError:
    print("Valor incorreto")

# Exemplo complexo CORRETO
# OBS: Você e responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except ValueError:
        return'Valor incorreto'
    except ZeroDivisionError:
        return 'Não é possível realizar uma divisão por zero'

num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")
print(dividir(num1, num2))

# Exemplo complexo - Genérico
# OBS: Você e responsável pelas entradas das suas funções. Então, trate-as!

def dividir(a, b):
    try:
        return int(a) / int(b)
    except:
        return 'Ocorreu um erro'

num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")
print(dividir(num1, num2))
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Exemplo complexo - Semi-Genérico
# OBS: Você e responsável pelas entradas das suas funções. Então, trate-as!


def dividir(a, b):
    try:
        return int(a) / int(b)
    except (ValueError, ZeroDivisionError) as err:
        return f'Ocorreu um problema: {err}'


num1 = input("Informe o primeiro número: ")
num2 = input("Informe o segundo número: ")
print(dividir(num1, num2))
