"""
Teste de Velocidade com Expressões Geradoras


def nums():
    for num in range(1, 10):
        yield num


ge1 = nums()
print(ge1)  # Generator
print()

print(next(ge1))
print(next(ge1))
print()

# Generator Expression
ge2 = (num for num in range(1, 10))

print(ge2)
print()

print(next(ge2))
print(next(ge2))
print()


"""
import os  # pacote de integração com o sistema operacional.
# Realizando o teste de velocidade
import time

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Generator Expression
gen_inicio = time.time()
print(sum((num for num in range(100000000))))  # 100 milhões
gen_tempo = time.time() - gen_inicio
print()

# List Comprehension
list_inicio = time.time()
print(sum([num for num in range(100000000)]))  # 100 milhões
list_tempo = time.time() - list_inicio
print()
print(f'Generator Expression levou {gen_tempo}')
print()
print(f'List Comprehension levou {list_tempo}')
print()
