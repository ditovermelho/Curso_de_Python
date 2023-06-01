""" 
Generator Expression

Em aulas anteriores nós estudamos:
- List Comprehension;
- Dictionary Comprehension;
- Set Comprehension;

Não vimos:
- Tuple Comprehension ... porque elas se chamam Generators

nomes = ['Carlos', 'Camila', 'Carla', 'Cassiano', 'Cristina', 'Vanessa']

print(any([nome[0] == 'C' for nome in nomes]))

# Poderíamos ter feito utilizando Generators

print(any(nome[0] == 'C' for nome in nomes))
print()

# List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(res)
print(type(res))
print()

# Generators
res = (nome[0] == 'C' for nome in nomes)
print(res)
print(type(res))
print()

# Mostra quantos bytes a string 'Geek' está ocupando em memória. Quanto maior a string, mais espaço ocupado.
print(getsizeof('Geek'))

print(getsizeof('University'))

print(getsizeof(9))

print(getsizeof(91))

print(getsizeof(92345668823))

print(getsizeof(True))
print()

# Gerando uma lista de números com List Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

# Gerando uma lista de números com Set Comprehension
set_comp = getsizeof({x*10 for x in range(1000)})

# Gerando uma lista de números com Dictionary Comprehension
dic_comp = getsizeof({x: x*10 for x in range(1000)})

# Gerando uma lista de números com Generator
gen = getsizeof(x*10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memória: ')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generator Expression: {gen} bytes')
print()
"""
import os  # pacote de integração com o sistema operacional.
# Qual é a utilidade de getsizeof()? -> Retorna a quantidade de bytes em memória do elemento passado como parâmetro
from sys import getsizeof

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None

# Eu posso iterar no Generator Expression? Sim!

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))
print()

for num in gen:
    print(num)

print()
