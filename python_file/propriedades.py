"""
POO - Propriedades - Properties

Em linguagens de programação como Java, ao declararmos atributos privados nas
classes, costumamos a criar métodos públicos para manipulação desses atributos.
Esses métodos são conhecidos por getters e setters, onde os getters retornam o
valor do atributo e os setters alteram o valor do mesmo.

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

    def get_numero(self):
        return self.__numero

    def set_titular(self, titular):
        self.__titular = titular

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def set_limite(self, limite):
        self.__limite = limite

    def get_limite(self):
        return self.__limite


conta1 = Conta("Felicity", 3000, 5000)
conta2 = Conta("Angelina", 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())
print()

# Forma incorreta de somar saldos
print(
    f'A soma do saldo das contas é {conta2._Conta__saldo + conta1._Conta__saldo}')
print()

# Forma correta de somar saldos
print(
    f'A soma do saldo das contas é {conta2.get_saldo() + conta1.get_saldo()}')
print()

print(conta1.extrato())
conta1.set_limite(999999)
print(conta1.extrato())
print()
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Refatorando a Classe utilizando propriedades.


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        Conta.contador += 1

    @property
    def numero(self):
        return self.__numero

    @property
    def titular(self):
        return self.__titular

    @property
    def saldo(self):
        return self.__saldo

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, novo_limite):
        self.__limite = novo_limite

    @property
    def valor_total(self):
        return self.__saldo + self.__limite

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


conta1 = Conta("Felicity", 3000, 5000)
conta2 = Conta("Angelina", 2000, 4000)

print(conta1.extrato())
print(conta2.extrato())
print()
print(
    f'A soma do saldo das contas é {conta2.saldo + conta1.saldo}')
print()
print(conta1.extrato())
conta1.limite = 76543
print(conta1.extrato())
print()
print(conta1.valor_total)
print(conta2.valor_total)
print()
