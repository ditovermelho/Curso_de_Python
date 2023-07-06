"""
Tipos de dados mais precisos

# Tipos comuns:
    - int;
    - str;
    - float;
    - list;
    - set;
    - dict;

# Tipos mais precisos:
    - Literal type;
    - Union;
    - Final;
    - Typed dictionaries;
    - Protocols;

# Teste mypy
mypy ./python_file/tipos_de_dados_mais_precisos.py


def dobro(valor: int) -> int:
    return valor * 2


print(dobro(8))
print(dobro(42))
print()

# Literal
from typing import Literal

def pegar_status(usuario: str) -> Literal['conectado', 'desconectado']:
    pass


def calcula_v1(opracao: str, num1: int, num2: int) -> str:
    if opracao == '+':
        return f'{num1} + {num2} = {num1 + num2}'
    elif opracao == '-':
        return f'{num1} - {num2} = {num1 - num2}'
    else:
        raise ValueError(f'Operação inválida {opracao!r}')


print(calcula_v1('+', 6, 4))
print(calcula_v1('-', 10, 2))
print(calcula_v1('*', 3, 5))

def calcula_v2(opracao: Literal['+', '-'], num1: int, num2: int) -> str:
    if opracao == '+':
        return f'{num1} + {num2} = {num1 + num2}'
    elif opracao == '-':
        return f'{num1} - {num2} = {num1 - num2}'
    else:
        raise ValueError(f'Operação inválida {opracao!r}')


print(calcula_v2('+', 6, 4))
print(calcula_v2('-', 10, 2))
print(calcula_v2('*', 3, 5))

# Union
from typing import Union

def soma(num1: int, num2: int) -> Union[str, int]:
    resultado: int = num1 + num2

    if resultado > 50:
        return f'O valor {resultado} é  muito grande'
    else:
        return resultado

# Final
from typing import Final

NOME: Final = 'Geek'
print(NOME)
NOME = 'University'
print(NOME)

from typing import final

@final
class Pessoa:
    pass


class Estudante(Pessoa):
    pass

    @final
    def estudar(self):
        return 'Estou estudando'


class Estagiario(Estudante):

    def estudar(self):
        return f'{super().estudar()} e estagiando'

# Typed dictionaries
from typing import TypedDict

class CursoPython(TypedDict):
    versao: str
    atualizacao: int


geek = CursoPython(versao='3.8.5', atualizacao=2020)
print(geek)
print()

ourto = CursoPython(algo='vai', coisa=True)
print(ourto)
print()

# Protocols
from typing import Protocol

"""
import os  # pacote de integração com o sistema operacional.
from typing import Protocol

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Curso(Protocol):
    titulo: str


def estudar(valor: Curso) -> None:
    print(f'Estou estudando o curso {valor.titulo}')


class Venda():
    def __init__(self, titulo) -> None:
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo


class Venda2(Curso):
    def __init__(self, titulo) -> None:
        super().__init__()
        self.__titulo = titulo

    @property
    def titulo(self):
        return self.__titulo


v1 = Venda('Programação em Python')
estudar(v1.titulo)
v2 = Venda2('Programação em Python')
estudar(v2.titulo)
