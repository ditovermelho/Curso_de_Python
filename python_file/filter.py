""" 
Filter

filter() -> Serve para filtrar dados de uma determinada coleção.

# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizado a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')
print()

# OBS: Assim como a função map(), a filter() recebe dois parâmetros, sendo
# uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(type(res))
print(list(res))
print()
print(f'Novamente: {list(res)}')
print()

# OBS: Assim como na função map(), após serem utilizados os dados de filter() eles são excluídos da memória.

paises = ['', 'Argentina', '', 'Brasil', 'Chile', '',
          'Colombia', '', 'Equador', '', '', 'Venezuela']

print(paises)
print()

res = filter(None, paises)
# res2 = filter(lambda pais: len(pais) > 0, paises)
# res3 =  filter(lambda pais: pais != '', paises)

print(list(res))
print()
# print(list(res2))
# print()

# A diferenção entre map() e filter() é
# map() -> recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para cada elemento do 
# iterável
# filter() -> Recebe dois parâmetros, uma função e um iterável e retorna um objeto filtrando apenas os elementos de 
# acordo com a função.

# Exemplos mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": [
        "Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
print()

# Filtrar os usuários estão inativos no Twitter

# Forma 1
# inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)
print()

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Combinado filter() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua instrutora é' + nome, desde que nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua instrutora é {nome}', filter(
    lambda nome: len(nome) < 5, nomes)))

print(lista)
print()
