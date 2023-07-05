"""
# Suit (Cards Deck) Symbols
site: https://www.alt-codes.net/suit-cards.php

# Execução
python ./python_file/jogo_cartas_v2.py

# Teste mypy
mypy ./python_file/jogo_cartas_v2.py

"""
import os  # pacote de integração com o sistema operacional.
import random
from typing import Dict, List, Tuple

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

NAIPES: List[str] = '♠ ♥ ♣ ♦'.split()
CARTAS: List[str] = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
CARTA = Tuple[str, str]
BARALHO = List[CARTA]


def criar_baralho(aleatorio: bool = False) -> BARALHO:
    """Criar um baralho com 52 cartas

    Args:
        aleatorio (bool, optional): variável de controle. Defaults to False.

    Returns:
        BARALHO: retorna o baralho com 52 cartas.
    """
    baralho: BARALHO = [(n, c) for c in CARTAS for n in NAIPES]

    if aleatorio:
        random.shuffle(baralho)
    return baralho


def distribuira_cartas(
    baralho: BARALHO
) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    """Gerencia a mão de cartas de acordo com o baralho gerado

    Args:
        baralho (BARALHO): baralho gerado

    Returns:
        Tuple[BARALHO, BARALHO, BARALHO, BARALHO]: retorna a mão de cartas
        gerenciada
    """
    return (baralho[0::4], baralho[1::4], baralho[2::4], baralho[3::4])


def jogar() -> None:
    """Inicia um jogo de cartas para 4 jogadores aleatoriamente
    """
    baralho: BARALHO = criar_baralho(aleatorio=True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {n: m for n, m in zip(
        jogadores, distribuira_cartas(baralho))}

    for jogador, cartas in maos.items():
        carta: str = ' '.join(f"{j}{c}" for (j, c) in cartas)
        print(f'{jogador}: {carta}')


if __name__ == '__main__':
    jogar()
