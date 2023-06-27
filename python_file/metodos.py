"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as
ações que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos
de Classe.

# Métodos de Instância.

# O método dunder init __init__ é um método especial chamado de construtor e
sua função é construir o objeto a partir da classe.

OBS: Todo elemento em Python que inicia a finaliza com duplo underline é
chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

Atenção! Por mais que possamos criar nossas próprias funções utilizando dunder
(underline no início e no final) não é aconselhado. Python possui vários
métodos com esta forma de nomenclatura e pode ser que mudemos o comportamento
dessas funções mágicas internas da linguagem. Então, evite ao máximo. De
preferência nunca o faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome
terá as palavras separadas por underline.

# Exemplos

p1 = Produto('PlayStation 4', 'Video Game', 2300)

print(p1.desconto(50))
print()
print(Produto.desconto(p1, 40)) # self, desconto
print()

user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Falicity', 'Jones', 'felicity@gmail.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())
print(Usuario.nome_completo(user1))
print()

# Acesso de forma errada de um atributo de classe
print(f'Senha: {user1._Usuario__senha}')
print(f'Senha: {user2._Usuario__senha}')
print()

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe a senha: ')
confirma_senha = input('Confirme a senha: ')

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senhas não conferem!')
    os._exit(1)

print("Usuário criando com sucesso!")

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print("Acesso permitido")
else:
    print('Acesso negado')
    os._exit(1)

print(f'Senha User Criptografada: {user._Usuario__senha}')  # Acesso errado

# Métodos de Classe em Python são conhecidos como Estáticos em outras
linguagens.

# Métodos de Classe

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta
print()

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user._Usuario__gera_usuario())  # Acesso, de forma ruim...

"""
import os  # pacote de integração com o sistema operacional.

from passlib.hash import pbkdf2_sha256 as crpy

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, numero, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor) -> None:
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, porcentagem):
        """Retorna o valor do produto com o desconto

        Args:
            porcentagem (_type_): porcentagem do desconto

        Returns:
            _type_: retorna o valor do desconto
        """
        return (self.__valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuários no sistema')

    @classmethod
    def ver(cls):
        print('Teste')

    @staticmethod
    def definicao():
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha) -> None:
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = crpy.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuário criado: {self.__gera_usuario()}')

    def correr(self, metros):
        return f'{self.__nome} está correndo {metros} metros'

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if crpy.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Método Estático

print(Usuario.contador)
print(Usuario.definicao())

user = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '123456')

print(user.contador)
print(user.definicao())
