"""
Tipos em Comentários

# Teste mypy
mypy ./python_file/tipos_comentarios.py
"""
import math
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Forma 1 - Recomendada/mais usual


def circunferencia(raio: float) -> float:
    """ função de calculo da circunferência.

    Args:
        raio (float): valor de raio passado.

    Returns:
        float: retorna o resultado do calculo da circunferência.
    """
    return 2 * math.pi * raio


print(circunferencia(8))
print()

# Forma 2 - Não muito usual/recomendado


def cabecalho(texto, alinhamento=True):
    # type: (str, bool) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


nome: str = 'Geek University'
print(cabecalho(nome))
print()
print(cabecalho(nome, False))
print()

# Forma 3 - Menos usual


def cabecalho2(
    texto,  # type: str
    alinhamento=True  # type: bool
):  # type: (...) -> str
    if alinhamento:
        return f"{texto.title()}\n{'-' * len(texto)}"
    else:
        return f" {texto.title()} ".center(50, '#')


print(cabecalho2(nome))
print()
print(cabecalho2(nome, False))
print()
