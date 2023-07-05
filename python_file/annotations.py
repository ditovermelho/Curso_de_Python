"""
Annotations - Type Hinting

Annotations ajudam a ter um type hinting e um código melhor.

# Exemplos

# Correto - Declaração
texto: str

# Incorreto - Declaração
texto : str
texto:str

# Correto - Retorno
) -> str:

# Incorreto - Retorno
)->str:
) ->str:

# Correto - Inicialização
alinhamento: bool = True

# Incorreto - Inicialização
alinhamento:bool=True
alinhamento : bool = True
alinhamento: bool= True

print(circunferencia.__annotations__)
print()

nome: str = 'Geek University'
peso: float = 67.9
ativo: bool = True

print(__annotations__)
print()
"""
import math
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def circunferencia(raio: float) -> float:
    return 2 * math.pi * raio


class Pessoa:

    def __init__(self, nome: str, idade: int, peso: float) -> None:
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def idade(self) -> int:
        return self.__idade

    @property
    def peso(self) -> float:
        return self.__peso

    def andar(self) -> str:
        return f'{self.nome} está andando'


p = Pessoa("Geek University", 37, 69.5)
print(p.__dict__)
print()
# print(p.__annotations__) # A instancia não tem annotations
print(p.__init__.__annotations__)
print(p.andar.__annotations__)
print()
