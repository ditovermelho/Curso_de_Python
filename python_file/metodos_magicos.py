"""
POO - Métodos Mágicos

Métodos Mágicos, são todos os métodos que utilizam dunder.

# dunder init -> __init__()

Dunder -> Double Underscore

# dunder repr -> Representação do objeto
def __repr__(self) -> str:
        return f'O livro {self.__titulo} possui {self.__paginas} paginas e foi escrito por {self.__autor}'

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Livro:

    def __init__(self, titulo, autor, paginas) -> None:
        self.__titulo = titulo
        self.__autor = autor
        self.__paginas = paginas

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def paginas(self):
        return self.__paginas

    def __str__(self) -> str:
        return f'O livro {self.__titulo} possui {self.__paginas} paginas e foi escrito por {self.__autor}'

    def __len__(self):
        return self.__paginas

    def __del__(self):
        return "Um objeto do tipo livro foi deletado da memória"

    def __add__(self, outro):
        return f'{self} - {outro}'

    def __mul__(self, outro):
        if isinstance(outro, int):
            msg = ''
            for n in range(outro):
                msg += ' ' + str(self)
            return msg
        return 'Não posso multiplicar'


livro1 = Livro('Python Rocks!', "Geek University", 400)
livro2 = Livro('Inteligência Artificial com Python', 'Geek University', 350)

print(livro1)
print(livro2)
print()
print(len(livro1))
print(len(livro2))
print()
print(livro1 + livro2)
print(livro1 * 3)
print()
