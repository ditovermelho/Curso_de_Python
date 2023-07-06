import os  # pacote de integração com o sistema operacional.
from time import sleep
from typing import Dict, List

from models.produto import Produto
from utils.helper import formata_float_str_moeda

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

produtos: List[Produto] = []
carrinho: List[Dict[Produto, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    os.system('cls') or None

    print(f"{'=' * 50}")
    print(f" Bem-vindo(a) ".center(50, '='))
    print(f" Geek Shop ".center(50, '='))
    print(f"{'=' * 50}")

    print('\nSelecione uma opção abaixo: ')
    print("1 - Cadastrar produto")
    print("2 - Listar produto")
    print("3 - Comprar produto")
    print("4 - Visualizar carrinho")
    print("5 - Fechar pedido")
    print("6 - Sair do sistema\n")

    opcao: int = int(input())

    match opcao:
        case 1:
            cadastrar_produto()
        case 2:
            listar_produto()
        case 3:
            comprar_produto()
        case 4:
            visualizar_carrinho()
        case 5:
            fechar_pedido()
        case 6:
            print('Volte sempre!\n')
            sleep(2)
            exit(0)
        case _:
            print('Opção invalida!')
            sleep(2)
            menu()


def cadastrar_produto() -> None:
    os.system('cls') or None
    print(f"{'=' * 50}")
    print(' Cadastro de Produto '.center(50, '='))
    print(f"{'=' * 50}")

    nome: str = input('Informe o nome do produto: ')
    preco: float = float(input('Informe o preço do produto: '))

    produto: Produto = Produto(nome, preco)

    produtos.append(produto)

    print(f'\nO produto {produto.nome} foi cadastrado com sucesso!\n')
    sleep(2)
    menu()


def listar_produto() -> None:
    os.system('cls') or None

    if len(produtos) > 0:
        print(f"{'=' * 50}")
        print(' Listagem de produtos '.center(50, '='))
        print(f"{'=' * 50}")
        for produto in produtos:
            print(produto)
            print(f"{'-' * 50}")
            sleep(1)
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem produtos cadastrados. '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def comprar_produto() -> None:
    os.system('cls') or None
    if len(produtos) > 0:
        print(f"{'=' * 70}")
        print(' Informe o código do produto que deseja adicionar ao carrinho: '.center(
            70, '='))
        print(f"{'-' * 70}")
        print(' Produtos Disponíveis '.center(70, '='))
        for produto in produtos:
            print(produto)
            print(f"{'-' * 70}")
            sleep(1)
        codigo: int = int(input())

        produto: Produto = pegar_produto_por_codigo(codigo)
        if produto:
            if len(carrinho) > 0:
                tem_no_carrinho: bool = False
                for item in carrinho:
                    quant: int = item.get(produto)
                    if quant:
                        item[produto] = quant + 1
                        print(
                            f'O produto {produto.nome} agora possui {quant + 1} unidades no carrinho.')
                        tem_no_carrinho = True
                        sleep(2)
                        menu()
                if not tem_no_carrinho:
                    prod = {produto: 1}
                    carrinho.append(prod)
                    print(
                        f'nO produto {produto.nome} foi adicionado ao carrinho.')
                    sleep(2)
                    menu()
            else:
                item = {produto: 1}
                carrinho.append(item)
                print(
                    f'\nO produto {produto.nome} foi adicionado ao carrinho.')
                sleep(2)
                menu()
        else:
            print(f"{'-' * 50}")
            print(
                f'O produto com código {codigo} não foi encontrado.')
            print(f"{'-' * 50}")
            sleep(2)
            menu()
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem produtos para vender. '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def visualizar_carrinho() -> None:
    os.system('cls') or None
    if len(carrinho) > 0:
        print(f"{'=' * 50}")
        print(' Produtos no Carrinho: '.center(50, '='))
        print(f"{'=' * 50}")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                print(f"{'-' * 50}")
                sleep(1)
    else:
        print(f"{'-' * 50}")
        print(" Ainda não existem produtos no carrinho. ".center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def fechar_pedido() -> None:
    os.system('cls') or None

    if len(carrinho) > 0:
        valor_total: float = 0

        print(f"{'=' * 50}")
        print(' Produtos no Carrinho '.center(50, '='))
        print(f"{'=' * 50}")

        for item in carrinho:
            for dados in item.items():
                print(dados[0])
                print(f'Quantidade: {dados[1]}')
                valor_total += dados[0].preco * dados[1]
                print(f"{'-' * 50}")
                sleep(1)
        print(f'Sua fatura é {formata_float_str_moeda(valor_total)}')
        print('Volte sempre!')
        carrinho.clear()
        sleep(5)
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem produtos no carrinho. '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def pegar_produto_por_codigo(codigo: int) -> Produto:
    p: Produto = None

    for produto in produtos:
        if produto.codigo == codigo:
            p = produto
    return p


if __name__ == '__main__':
    main()
