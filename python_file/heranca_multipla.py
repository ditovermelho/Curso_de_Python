"""
POO - Herança Múltipla

Herança Múltipla nada mais é do que a possibilidade de uma classe herdar de
múltiplas classe, fazendo com que a classe filha todos os atributos e métodos
de todas classe herdadas.

# OBS: A herança múltipla pode ser feita de duas maneiras:
    - Por Multiderivação Direta;
    - Por Multiderivação Indireta;

# Exemplo 1 - Mutiderivação Direta


class Base1:
    pass


class Base2:
    pass


class Base3:
    pass


class MultiDerivada(Base1, Base2, Base3):
    pass

# Exemplos 2 - Multiderivação Indireta


class Base1:
    pass


class Base2(Base1):
    pass


class Base3(Base2):
    pass


class MultiDerivada(Base3):
    pass

# OBS: Não importa se a derivação é direta ou indireta. A classe que realiza a
herança herdará todos atributos e métodos das super classes. 
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Animal:

    def __init__(self, nome) -> None:
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome

    def cumprimentar(self):
        return f'Eu sou {self.__nome}'


class Aquatico(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def nadar(self):
        return f'{super().nome} está nadando.'

    def cumprimentar(self):
        return f'{super().cumprimentar()} do mar'


class Terrestre(Animal):

    def __init__(self, nome) -> None:
        super().__init__(nome)

    def andar(self):
        return f'{super().nome} está andando.'

    def cumprimentar(self):
        return f'{super().cumprimentar()} da terra'


class Pinguim(Terrestre, Aquatico):

    def __init__(self, nome) -> None:
        super().__init__(nome)


# Testando

baleia = Aquatico('Wally')
print(baleia.nadar())
print(baleia.cumprimentar())
print()

tatu = Terrestre('Xim')
print(tatu.andar())
print(tatu.cumprimentar())
print()

tux = Pinguim('Tux')
print(tux.andar())
print(tux.nadar())
# Method Resolution Order - MRO
print(tux.cumprimentar())
print()

# Objetos é instância de ...

print(f'Tux é instancia de Pinguim? {isinstance(tux, Pinguim)}')
print(f'Tux é instancia de Aquatico? {isinstance(tux, Aquatico)}')
print(f'Tux é instancia de Terrestre? {isinstance(tux, Terrestre)}')
print(f'Tux é instancia de Animal? {isinstance(tux, Animal)}')
print(f'Tux é instancia de objeto? {isinstance(tux, object)}')
print()
