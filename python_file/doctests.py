"""
Doctest

Doctests são testes que colocamos na docstring das funções/métodos Python

python -m doctest -v ./python_file/doctests.py

def soma(a, b):
    ''''''Soma os números a e b

    Args:
        a (int/float): valor a
        b (int/float): valor b

    Returns:
        int/float: retorna a soma de a + b

    #>>> soma(1,2)
    3

    #>>> soma(4,6)
    10
    ''''''
    return a + b

Trying:
    soma(1,2)        
Expecting:
    3
ok
Trying:
    soma(4,6)        
Expecting:
    10
ok
1 items had no tests:
    doctests
1 items passed all tests:
   2 tests in doctests.soma
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


# Outro Exemplo, Aplicando o TDD

def duplicar(valores):
    """Duplica os valores em uma lista

    Args:
        valores (list): lista para ser duplicada

    >>> duplicar([1, 2, 3, 4])
    [2, 4, 6, 8]

    >>> duplicar([])
    []
    >>> duplicar(['a', 'b', 'c'])
    ['aa', 'bb', 'cc']
    >>> duplicar([True, None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * elementos for elementos in valores]

# Erro inesperado...
# OBS: Dentro do doctest, o Python não reconhece string com aspas duplas.
# Precisa ser aspas simples.


def fala_oi():
    """Fala oi

    Returns:
        string: retorna oi

    >>> fala_oi()
    'oi'
    """
    return 'oi'

# Um último caso estranho...


def verdade():
    """Retorna Verdade

    Returns:
        Bool: retorna verdade

    >>> verdade()
    True
    """
    return True
