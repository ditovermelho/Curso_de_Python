"""
Type Hinting

Mesmo que os tipos sejam definidos no começo da função, isso não vai impedir de
que a função seja inicializada com tipos diferentes dos declarados. Essa
declaração seve para facilitar a visualização do que a função espera e retorna,
tanto para compilador quanto para o programador.

# Verificação com mypy
mypy ./python_file/type_hinting.py

A utilização de type hinting facilita o interpretação das ides para
identificação de suas função, mas isso pode causar uma queda no tempo de
execução do código python.


"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def cumprimentar(nome: str) -> str:
    """cumprimentar

    Args:
        nome (str): nome

    Returns:
        str: retorna Olá, {nome}
    """
    return f'Olá, {nome}'


print(cumprimentar('Geek'))
print()


def cabecalho(texto: str, alinhamento: bool = True) -> str:
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


cabeca = 'Geek University'
print(cabecalho(cabeca))
print()
print(cabecalho(cabeca, False))
print()
# print(cabecalho(cabeca, alinhamento="True"))
# print()
