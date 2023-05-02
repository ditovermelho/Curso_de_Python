""" 
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência á teoria dos conjuntos
da Matemática.

- No Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:

- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Qunado não precisamos se preocupar
com chavesm valores e itens duplicados.

Os conjuntos (stes) são referenciados em Python com chaves {}

Diferença entre conjuntos (Set)  e Mapas (dicionários)  em Python;
   - Um dicionário tem chave/valor;
   - Um conjuntotem apenas valor;


# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos.

print(s, '\n')
print(type(s), '\n')

# OBS: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}

print(s, '\n')
print(type(s), '\n')

# Podemos verificar se determinado elemento está contido no conjunto

valor = 3

if valor in s:
    print(f'Tem o {valor}', '\n')
else:
    print(f'Não tem o {valor}', '\n')

# Importante lembrar que , além de não termos valores duplicados, não temos ordem
dados = [99, 2, 34, 2, 23, 12, 1, 44, 5, 34]

# Listas aceitam valores duplicados, então temos 10 elementos
lista = list(dados)
print(f'Lista: {lista} com {len(lista)} elementos', '\n')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = tuple(dados)
print(f'Tupla: {tupla} com {len(tupla)} elementos', '\n')

# Dicionario não aceitam valores duplicados, então temos 8 elementos
dicionario = {}.fromkeys(dados, 'dict')
print(f'Dicionario: {dicionario} com {len(dicionario)} elementos', '\n')

# Conjunto não aceitam valores duplicados, então temos 8 elementos
s = set(dados)
print(f'Conjunto: {s} com {len(s)} elementos', '\n')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente.
for valor in s:
    print(valor)

# Usos interessantes com sets.
# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nos adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande',
           'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']
print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidades distintas, ou seja únicas, temos.
# O que você daria? Faria um lop na lista......?
# Podemos utilizar o set para isso:

print(len(set(cidades)))

# Adicionando elementos em um conjunto
s = {1, 2, 3}

s.add(4)
# Duplicidade não gera erro. Simplesmente é ignorado e não é adicionado.
s.add(4)
print(s)

# removendo elementos em um conjunto

# Forma 1

ret = s.remove(3)  # Não é indice! Informamos o varlor a ser removido.
print(ret)
print(s)

# OBS: Caso o valor não seja encontrado sera gerado o erro KeyError.
# Nem um valor e retornado.

# Forma 2

s.discard(2)

print(s)

# OBS: Se o valor não for encontrado, nem um erro é gerado.

# Copiando um conjunto para ouro ...

# Forma 1 - Deep Copy

novo = s.copy()
print(novo, '\n')

novo.add(4)
print(novo, '\n')
print(s, '\n')

# Forma 2 - Shallow Copy

novo = s
print(novo, '\n')

novo.add(4)
print(novo, '\n')
print(s, '\n')

# Podemos remover todos os item de um conjunto

s.clear()
print(s, '\n')

# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contedo estudadentes do Curso de Python e um
# contendo estudantes do curso de Java.

estudates_python = {'Marcos', 'Patricia',
                    'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudates_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.
# Precisamos gerar um conjunto com nomes de estudantes únicos.
# Forma 1 - Utilizando union

unicos1 = estudates_python.union(estudates_java)
# unicos1 = estudates_java.union(estudates_python)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |
unicos2 = estudates_java | estudates_python
print(unicos2)

 Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection

ambos1 = estudates_python.intersection(estudates_java)
print(ambos1)

# Forma 2- Utilizando o &

ambos2 = estudates_python & estudates_java
print(ambos2)

# Gerarum conjunto de estudantes que não estão no outro curso

so_python = estudates_python.difference(estudates_java)
print(so_python)

so_java = estudates_java.difference(estudates_python)
print(so_java)

"""

# Métodos Matemáticos de Conjuntos
# Imagine que temos dois conjuntos: Um contedo estudadentes do Curso de Python e um
# contendo estudantes do curso de Java.

estudates_python = {'Marcos', 'Patricia',
                    'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudates_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho
# * Se os valores forem inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
