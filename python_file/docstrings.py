"""
Documentando funções com Docstrings
OBS: Podemos ter acesso a documentação de uma em Python utilizando a propriedade especial __doc__
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


print(diz_oi(), '\n')
help(diz_oi)
print(diz_oi.__doc__, '\n')


def exponencial(numero, potencia=2):
    """Função que retorna por padrão o quadrado de 'número' ou 'número' á 'potencia' informada.

    Args:
        numero (int): Número que desejamos gerar o exponencial.
        potencia (int, optional): Potência que queremos gerar o exponencial. Defaults to 2.
    Returns:
        int: Retorna o exponencial de 'número' por 'potencia'
    """

    return numero ** potencia


def soma(a, b):
    """Função que retorna a soma de 'a' e 'b'

    Args:
        a (int): Número que desejamos Somar
        b (int): Número que desejamos Somar

    Returns:
        int: Retorna a soma de 'a' e 'b'
    """
    return a + b
