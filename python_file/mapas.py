""" 
Mapas -> Chonecidos em Python como Dicionários 

Dicionarios em Python são representados por chaves {}

recitas = {'jan': 100, 'fer': 250, 'mar': 400}

print(recitas)

# Interar sobre dicionários

for chave in recitas:
    print(chave, '\n')

for chave in recitas:
    print(f'{chave} : {recitas[chave]}')
    
print(recitas.keys(), '\n')

for chave in recitas:
    print(recitas[chave])

# Acessando os valores

print(recitas.values(), '\n')

for valor in recitas.values():
    print(valor)

# Desempacotamento de dicionários

for chave, valor in recitas.items():
    print(f'chave = {chave} e valor = {valor}')


"""

recitas = {'jan': 100, 'fer': 250, 'mar': 400}


# Soma*, Valor Máximo*, Valor Minimo*, Tamanho
# * Se os valores forem todos inteiros ou reais

print(sum(recitas.values()))
print(max(recitas.values()))
print(min(recitas.values()))
print(len(recitas))
