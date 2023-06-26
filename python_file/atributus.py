"""
POO - Atributos

Atributos -> Representam as características do objetos. Ou seja, pelos
atributos nós conseguimos representar computacionalmente os estados de um
objeto.

Em Python, dividimos os atributos em 3 grupos:
    - Atributos de Instância;
    - Atributos de Classe;
    - Atributos Dinâmico;


# Atributos de instância: São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial utilizado para o construção do
objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais  ou menos:

public class Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }

    public int getVoltagem(){
        return this.voltagem
    }
}

Em Python, por convenção, ficou estabelecido que, todo atributo de uma classe é
público. Ou seja, pode ser acessado em todo projeto.

Caso queiramos demonstrar que determinado atributo deve ser tratado como
privado, ou seja, que deve ser acessado/utilizado somente dentro da própria
classe onde está declarado, utiliza-se __ duplo underscore no início de seu
nome.

Isso é conhecido também como Name Mangling.

# Classes com Atributo de Instância Publica


class Lampada:
    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:
    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:
    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:
    def __init__(self, nome, email, senha) -> None:
        self.nome = nome
        self.email = email
        self.senha = senha


class Teste:
    def __init__(cerveja, nome, idade) -> None:
        cerveja.nome = nome
        cerveja.idade = idade

# Atributos Públicos e Atributos Privados


class Acesso:
    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        return self.__senha

# OBS: Lembre-se que isso é apenas uma convenção, ou seja, a linguagem Python
não vai impedir que façamos acesso aos atributos sinalizados como privados fora
da classe.


user = Acesso('user@gmail.com', '123456')

print(dir(user))
print(user.email)
# print(user.__senha) #AttributeError
# Temos acesso. MAs não deveríamos fazer este acesso
print(user._Acesso__senha)
print(user.mostra_senha())
print()

# O que significa atributos de instância?
Significa, que ao criarmos instâncias/objetos de uma classe, todas as
instâncias terão estes atributos.

user1 = Acesso('user1@gmail.com', '123456')
user2 = Acesso('user2@gmail.com', '678910')

print(user1.email)
print(user2.email)
print()

# Atributos de Classe

p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

# Atributos de Classe, são atributos, claro, que são declarados diretamente na
classe, ou seja fora do construtor. Geralmente já inicializamos um valor, e
este valor é compartilhado entre todas as instâncias da classes. Ou seja, ao
invés de cada instancia, da classe ter seus próprios valores com é o caso dos
atributos de instância, com os atributos de classe todas as instâncias terão o
mesmo valor para este atributo.

# Refatorando a classe Produto


class Produto:
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Xbox S', 'Video game', 4500)

print(p1.imposto)
print(p2.imposto)
print()
print(p1.valor)  # Acesso possível, mas incorreto de um atributo de classe
print(p2.valor)  # Acesso possível, mas incorreto de um atributo de classe
print()

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso de
classe

print(Produto.imposto)  # Acesso correto de um atributo de classe
print()
print(p1.id)
print(p2.id)
print()

# OBS: Em linguagens coma Java, os atributos conhecidos como atributos de
classe, em Python são chamados de atributos estáticos;

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Produto:
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


# Atributos Dinâmicos -> Um atributo de instância pode ser criado em tempo de
# execução.

# OBS: O atributo dinâmico sera exclusivo da instância que o criou.

p1 = Produto('PlayStation 4', 'Video game', 2300)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

p2.peso = '5kg'  # Note que na classe Produto não existe o atributo peso.

print(
    f'Produto: {p2.nome}, Descrição: {p2.descricao}, Valor: {p2.valor}, Peso: {p2.peso}')
# print(f'Produto: {p1.nome}, Descrição: {p1.descricao}, Valor: {p1.valor}, Peso: {p1.peso}')

# Deletando atributos

print(p1.__dict__)
print(p2.__dict__)
print()

del p2.peso

print(p1.__dict__)
print(p2.__dict__)
print()
