"""
Tipo Numérico
"""

num = 1_000_000
print(float(num))

"""
Tipo Float

tipo real, decimal

OBS: o separador de casas decimais na progamação é o ponto e não a vírgula
"""

# Errada
valor - 1, 44
print(valor)
print(type(valor))

# Certo
valor = 1.44
print(valor)
print(type(valor)

# é possivel
valor1, valor2 = 1, 44
print(valor)
print(type(valor1))
print(valor)
print(type(vallor2))

# Podemos converter tipo float para int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão
"""
res = int(valor)
print(res)
print(type(res))

# Podemos trabalhar com números complexos
variavel = 5j

"""
Tipo booleano

Álgebra Booleana, criada por George Boole

2 constantes, Verdadeiro ou Faldo

True -> Verdadeiro
False -> Faldo

OBS: Sempre com a inicial mainúscula

Errado:

true, false

Certo:

True, False
"""

ativo = True

print(ativo)

"""
Operações básicas
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso, se for falso o resultado sera verdadeiro.
Ou seja, sempre o contrário. 
"""

print(not ativo)

logado = False

# Ou (or):
"""
É uma operação binária, ou seja, depende de dois valores. Ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# E (and):
"""
È uma operação binaria, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros

True and True -> True
True and False -> False
False and True -> False
False and False -> False
"""

"""
Tipo string

Em python, um dado é considerado do tipo string semque que:

- Estiver entre áspas simples -> 'uma string', '234', 'a', 'True', '42.3' 
- Estiver entre áspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre áspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3''' 
"""
# - Estiver entre áspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3""" 

"""
nome = 'carlos'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

nome = 'Angelina \nJoline'
print(nome)
print(type(nome))

print(nome.split()) # Transforma em uma lista de strings

print(nome[0:8]) # Slice de string

# [::-1] -> Comece do primeiro elemento, vá até o último elemento e inverta

print(nome[::-1]) # Inversão da String Pythônico

print(nome.replace('a', 'o'))

texto = 'socorram me subino onibus em marrocos' 
print(texto[::-1])

"""