"""
Preservando metadatas com wraps

Metadados -> São dados intrínsecos em arquivos.
wraps -> São funções que envolvem elementos com diversas finalidades.

# Problema


def ver_log(funcao):
    def logar(*args, **kwargs):
        # Eu sou uma função (logar) dentro de outra
        #
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Está e a documentação: {funcao.__doc__}\n')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    #Soma dois números

    Args:
        a (real): valor da variável
        b (real): valor da variável

    Returns:
        real: a + b
    #
    return a + b


print(soma(10, 30))
print()

print(soma.__name__)  # Nome da função
print(soma.__doc__)  # Documentação da função
print()

"""
import os  # pacote de integração com o sistema operacional.
from functools import wraps

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Resolução do Problema


def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Eu sou uma função (logar) dentro de outra
        """
        print(f'Você está chamando a função: {funcao.__name__}')
        print(f'Está e a documentação: {funcao.__doc__}\n')
        return funcao(*args, **kwargs)
    return logar


@ver_log
def soma(a, b):
    """Soma dois números

    Args:
        a (real): valor da variável
        b (real): valor da variável

    Returns:
        real: a + b
    """
    return a + b


print(soma(10, 30))
print()

print(soma.__name__)  # Nome da função
print(soma.__doc__)  # Documentação da função
print()
