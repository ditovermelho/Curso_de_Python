"""
Erros mais comuns em Python

ATENÇÂO! É importante prestar atenção e aprender a ler as saídas de erros
gerados pela execução
do nosso código

Os erros mais comuns:

1 - SyntaxError -> Ocorre quando o Python encontra um erro de sintaxe. Ou seja,
você escreveu algo que
o Python não reconhece como parte da linguagem.

Exemplos SyntaxError

a) def função:
        print('Geek University')

b) def = 1

c) return

2 - NameError -> Ocorre quando uma variável ou função não foi definida.

Exemplos NameError

a) print(geek)
b) geek()
c) a = 8
if a < 10:
   msg = 'É maior que 10'

print(msg)

3 - TypeError -> Ocorre quando uma função/operação/ação é aplicada a um
tipo errado.

Exemplos de TypeError

a) print(len(5))
b) print('Geek' + [])

4 - IndexError -> Ocorre quando tentamos acessar um elemento em uma lista ou
outro tipo de dado indexado utilizando um índice inválido.

Exemplos de IndexError

a) lista = ['geek']
print(lita[2])
b)lista = ['Geek']
print(lista[0][10])
c) tupla = ('Geek')
print(tupla[0][10])

5 - ValueError -> Ocorre quando uma função/operação built-in (integrada)
recebe um argumento com correto mas valor inapropriado.

Exemplos de ValueError

a) print(int('geek'))

6 - KeyError -> Ocorre quando tentamos acessar um dicionário com uma chave
que não existe.

Exemplos de KeyError

a) dic = {}
print(dic['geek'])

7 - AttributeError ->  Ocorre quando uma variável não tem um atributo/função

Exemplos de KeyError

a) tupla = (11, 2, 31, 4)
print(tupla.sort())

8 - IndentationError -> Ocorre quando não respeitamos a indentação do Python
(4 espaços)

Exemplos de KeyError

a) def nova();
print('nova')
nova()

b) for i in range(10):
pint(i+1)

OBS: Exceptions e Erros são sinônimos na programação.
OBS: Importante ler e prestar atenção na saída de erro.
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None
