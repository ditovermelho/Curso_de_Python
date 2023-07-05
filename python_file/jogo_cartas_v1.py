"""
Tipos em Python na prática

nomes: list = ["Geek", 'University']
versoes: tuple = (3, 4, 7)
opcoes: dict = {'ar': True, 'banco_couro': True}
valores: set = {3, 4, 5, 6}

print(__annotations__)
print()

from typing import Dict, List, Set, Tuple

nomes: List[str] = ["Geek", 'University']
versoes: Tuple[int] = (3, 4, 7)
opcoes: Dict[str, bool] = {'ar': True, 'banco_couro': True}
valores: Set[int] = {3, 4, 5, 6}

print(__annotations__)
print()

# Suit (Cards Deck) Symbols
site: https://www.alt-codes.net/suit-cards.php

# Execução
python ./python_file/jogo_cartas_v1.py

"""
import os  # pacote de integração com o sistema operacional.
import random

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

NAIPES: list = '♠ ♥ ♣ ♦'.split()
CARTAS: list = '2 3 4 5 6 7 8 9 10 J Q K A'.split()


def criar_baralho(aleatorio: bool = False) -> list:
    """Criar um baralho com 52 cartas

    Args:
        aleatorio (bool, optional): variável de controle. Defaults to False.

    Returns:
        list: retorna o baralho com 52 cartas.
    """
    baralho: list = [(n, c) for c in CARTAS for n in NAIPES]

    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuira_cartas(baralho):
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar():
    cartas = criar_baralho(aleatorio=True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {n: m for n, m in zip(jogadores, distribuira_cartas(cartas))}

    for jogador, cartas in maos.items():
        carta = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
