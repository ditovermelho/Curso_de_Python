"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e
hierárquico utilizando classes.

Encapsular -> cápsula

        Classe
-------------------------
|                       |
|  Atributos de classe  |
|_______________________|

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo privado
chamado __nome e um método privado chamado __fala()

Esses elementos privados só devem/deveriam ser acessados dentro da classe. Mas
Python não bloqueia este acesso fora da classe. Com Python acontece um fenômeno
chamado Name Mangling, que faz uma alteração na forma de se acessar os
elementos privados, conforma:

_Classe__elemento

Exemplo - Acessando elementos privados fora da classe;

instancia._Pessoa__nome
instancia._Pessoa__fala()

Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe,
escondendo atributos e métodos privados de usuário.

# Testando

conta1 = Conta("Geek", 150.00, 1500)

print(conta1.checar_conta())
print()
print(conta1.extrato())
print()
conta1.sacar(151)
print()
conta1.depositar(150)
conta1.sacar(151)
print()

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    def checar_conta(self):
        return f'A conta de número: {self.__numero}, pertence ao Titular: {self.__titular}'

    def extrato(self):
        return f'Saldo {self.__saldo} do titular {self.__titular} com limite de {self.__limite}'

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            print('Deposito realizado com sucesso!\n')
        else:
            print('Valor invalido!\n')

    def sacar(self, valor):
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor
                print('Sace realizado com sucesso!\n')
            else:
                print('Saldo insuficiente!\n')
        else:
            print('Valor invalido!\n')

    def transferir(self, valor, conta_destino):
        # 1 - Remover valor da conta de origem
        if valor > 0:
            if valor <= self.__saldo:
                self.__saldo -= valor

                # 2 - Adicionar o valor na conta de destino
                conta_destino.__saldo += valor

                print('Operação realizada com sucesso\n')
            else:
                print('Saldo insuficiente!\n')
        else:
            print('Valor invalido!\n')


conta1 = Conta("Geek", 150.00, 1500)
conta2 = Conta("Angelina", 300.00, 2000)

print(conta1.extrato())
print(conta2.extrato())
print()

conta2.transferir(100, conta1)

print(conta1.extrato())
print(conta2.extrato())
print()
