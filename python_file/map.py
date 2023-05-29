""" 
Map

Com map, fazemos mapeamento de valores para função.

import math

def area(r):
    #Calcula a área de um círculo com raio r

    Args:
        r (tipo real): raio

    Returns:
        tipo real: retorna a área
    #
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))
print()


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []

for r in raios:
    areas.append((area(r)))

print(areas)
print()

# Forma 2 - Map
# Map e uma função que recebe dois parâmetros: O primero a função, o segundo um iterável

areas = map(area, raios)
print(areas)
print(type(areas))
print()
print(list(areas))
print()

# Forma 3 - Map com Lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))
print()

# OBS: Após utilizar a função map() depois do primeiro resultado, ele zera.
"""

import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno do comando
os.system('cls') or None


# Para fixar - Map
# Temos dados interáveis:
# dados: a1, a2, ..., an
# Temos uma função:
# Função: f(x)
# Utilizamos a função map(f, dados) onde map ira 'mapear' cada elementos dos dados e aplicar a função
# O Map object: f(a1), f(a2), f(...), f(an)

# Mais um exemplo

cidades = [('Berlim', 29), ('Cairo', 36), ('Buenos Aires', 19),
           ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28), ('Londes', 22)]

print()

# f = 9/5 * c + 32

# Lambda


def c_para_f(dado): return (dado[0], (9/5) * dado[1] + 32)


print(list(map(c_para_f, cidades)))
print()
