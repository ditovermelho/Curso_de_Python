"""
POO - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra
classe que passa a herdar atributos e métodos da classe herdada.

Cliente
    - nome;
    - sobrenome;
    - cpf;
    - renda;

Funcionario
    - nome;
    - sobrenome;
    - matricula;

Pergunta: Existe alguma entidade genérica o suficiente para encapsular os
atributos e métodos comuns a outras entidades?

class Cliente(Pessoa):

    def __init__(self, nome, sobrenome, cpf, renda) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__renda = renda
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Funcionario(Pessoa):
    def __init__(self, nome, sobrenome, cpf, matricula) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf
        self.__matricula = matricula
    
    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e
métodos da classe herdara.

Quando uma classe herda de outra classe, herdada é conhecida por:
    [Pessoa]
    - Super Classe;
    - Classe Mãe;
    - Classe Pai;
    - Classe Base;
    - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
    [Cliente, Funcionario]
    - Sub Classe;
    - Classe Filha;
    - Classe Específica;

# Refatorando as Classes.

class Pessoa:

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    Cliente herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, renda) -> None:
        # Forma incomum de acessar dados da super classe
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda


class Funcionario(Pessoa):
    Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula) -> None:
        # Forma comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print()
print(cliente1.__dict__)
print(funcionario1.__dict__)
print()

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método
presente na super classe em suas filhas.
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Pessoa:

    def __init__(self, nome, sobrenome, cpf) -> None:
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__cpf = cpf

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'


class Cliente(Pessoa):
    """Cliente herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, renda) -> None:
        # Forma incomum de acessar dados da super classe
        Pessoa.__init__(self, nome, sobrenome, cpf)
        self.__renda = renda

    def nome_completo(self):
        # Forma errada de fazer acesso a informações da classe super/mãe.
        return f'{self._Pessoa__nome} possui uma renda de {self.__renda} '


class Funcionario(Pessoa):
    """Funcionario herda de Pessoa"""

    def __init__(self, nome, sobrenome, cpf, matricula) -> None:
        # Forma comum de acessar dados da super classe
        super().__init__(nome, sobrenome, cpf)
        self.__matricula = matricula

    def nome_completo(self):
        # Forma correta de fazer acesso a informações da classe super/mãe.
        return f'Funcionário: {self.__matricula} Nome: {super().nome_completo()}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789-00', 5000)
funcionario1 = Funcionario('Felicity', 'Jones', '987.654.321-11', 1234)

print(cliente1.nome_completo())
print(funcionario1.nome_completo())
print()
