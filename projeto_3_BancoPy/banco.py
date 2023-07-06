import os  # pacote de integração com o sistema operacional.
from time import sleep
from typing import List

from models.cliente import Cliente
from models.conta import Conta

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    os.system('cls') or None

    print(f"{'=' * 50}")
    print(f" ATM ".center(50, '='))
    print(f" Geek Bank ".center(50, '='))
    print(f"{'=' * 50}")

    print('\nSelecione uma opção menu: ')
    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar depósito")
    print("4 - Efetuar transferência")
    print("5 - Listar contas")
    print("6 - Sair do sistema\n")

    opcao: int = int(input())

    match opcao:
        case 1:
            criar_conta()
        case 2:
            efetuar_saque()
        case 3:
            efetuar_deposito()
        case 4:
            efetuar_transfarencia()
        case 5:
            listar_contas()
        case 6:
            print('Volte sempre!\n')
            sleep(2)
            exit(0)
        case _:
            print('Opção invalida!')
            sleep(2)
            menu()


def criar_conta() -> None:
    os.system('cls') or None
    print(f"{'-' * 50}")
    print(' Informe os dados do cliente '.center(50, '='))
    print(f"{'-' * 50}")

    nome: str = input('Nome do cliente: ')
    email: str = input('E-mail do cliente: ')
    cpf: str = input('CPF do cliente: ')
    data_nascimento: str = input('Data de nascimento do cliente: ')

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)

    conta: Conta = Conta(cliente)

    contas.append(conta)

    print(f"{'-' * 50}")
    print(' Conta criada com sucesso. '.center(50, '='))
    print(' Dados da conta: '.center(50, '='))
    print(f"{'-' * 50}")
    print(conta, '\n')
    sleep(2)
    menu()


def efetuar_saque() -> None:
    os.system('cls') or None
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor do saque: '))

            conta.sacar(valor)
        else:
            print(f"{'-' * 50}")
            print(
                f' Não foi encontrada a conta com número {numero} '.center(50, '='))
            print(f"{'-' * 50}")
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem contas cadastradas '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def efetuar_deposito() -> None:
    os.system('cls') or None
    if len(contas) > 0:
        numero: int = int(input('Informe o número da sua conta: '))

        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input('Informe o valor de deposito: '))

            conta.depositar(valor)
        else:
            print(f"{'-' * 50}")
            print(
                f' Não foi encontrada a conta com número {numero} '.center(50, '='))
            print(f"{'-' * 50}")
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem contas cadastradas '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def efetuar_transfarencia() -> None:
    os.system('cls') or None
    if len(contas) > 0:
        numero_o: int = int(input('Informe o número da sua conta: '))

        conta_o: Conta = buscar_conta_por_numero(numero_o)
        if conta_o:
            numero_d: int = int(
                input('Informe o número da conta de destino: '))

            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(
                    input('Informe o valor da transferência: '))

                conta_o.transferir(conta_d, valor)
            else:
                print(f"{'-' * 70}")
                print(
                    f' A conta destino com número: {numero_d} não foi encontrada '.center(70, '='))
                print(f"{'-' * 70}")
    else:
        print(f"{'-' * 50}")
        print(' Ainda não existem contas cadastradas '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def listar_contas() -> None:
    os.system('cls') or None
    if len(contas) > 0:
        print(f"{'=' * 50}")
        print(' Listagem de contas '.center(50, '='))
        print(f"{'=' * 50}")

        for conta in contas:
            print(conta)
            print(f"{'-' * 50}")
            sleep(1)
    else:
        print(f"{'-' * 50}")
        print(' Não existem contas cadastradas '.center(50, '='))
        print(f"{'-' * 50}")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c


if __name__ == '__main__':
    main()
