"""
Levando os próprios erros com raise

raise -> Lança exceções

OBS: O raise não é uma função. É uma palavra reservada, assim como def ou
qualquer outra em Python.

Para simplificar, pense no raise como sendo útil para que possamos criar
nossas próprias exceções e mensagens de erro.

A forma geral de utilização é:

raise TipoDoErro('mensagem de erro')

# Exemplo real


def colore(texto, cor):
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    return f'O texto {texto} será impresso na cor {cor}'


texto, cor = ['Geek', 'azul']
print(colore(texto, cor))
print()

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Exemplo real


def colore(texto, cor):
    cores = ('verde', 'amarelo', 'azul', 'branco')
    if type(texto) is not str:
        raise TypeError('Texto precisa ser uma string')
    if type(cor) is not str:
        raise TypeError('Cor precisa ser uma string')
    if cor not in cores:
        raise ValueError(f'A Cor precisa ser uma entre: {cores}')
    return f'O texto {texto} será impresso na cor {cor}'


texto, cor = ['Geek', 'preto']
print(colore(texto, cor))
print()
