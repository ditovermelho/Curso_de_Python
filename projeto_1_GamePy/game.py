import os  # pacote de integração com o sistema operacional.

from models.calcular import Calcular

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    dificuldade: int = int(
        input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: '))

    calc: Calcular = Calcular(dificuldade)

    print('Informe o resultado para a seguinte operação: ')
    print(calc.mostrar_operacao() + ' ?')

    resultado: int = int(input())
    print()

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} ponto(s).\n')

    continuar: int = int(
        input('Deseja continuar no jogo? [1 - sim, qualquer outro valor - não] '))
    print()

    if continuar == 1:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()
