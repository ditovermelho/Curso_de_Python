"""
Entendendo Iterators e Iterables

Iterator -> 
    - Um objeto que pode ter iterado.
    - Um objeto que retorna um dado, sendo um elemento por vez quando uma
    função next() é chamada;

Iterable ->
    - Um objeto que irá retornar um iterator quando a função iter() for 
    chamada.

nome = 'Geek'  # É um iterable mas não é um iterator.
numeros = [1, 2, 3, 4, 5, 6]  # É um iterable mas não é um iterator.

it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))
print()

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))
print()

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

nome = 'Geek'

for letra in nome:
    print(f'{letra}')
