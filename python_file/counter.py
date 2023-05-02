""" 
Módulo Collections - Counter

Collections -> High-performance Container Datetypes

Counter -> Recebe um interável como parâmetro e cria um objeto do tipo Collections Couter que é parecido
com um dicionário, contendo como chave o elemento da lista passada como parâmetro e como calor a quantidade
de ocorrências desse elemento.

# Realizando o import

from collections import Counter

# Exemplo 1 

# Podemos utilizar qualquer interável, aqui usamos uma lista
lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 5, 3, 45, 45, 66, 66, 43, 34]

# Utilizando o Counter
res = Counter(lista)

print(type(res))
print(res)

# Counter({1: 5, 3: 5, 2: 4, 5: 4, 4: 3, 45: 2, 66: 2, 43: 1, 34:1})

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como valor a quantidade de ocorrências.

# Exemplo 2

print(Counter('Geek University'))
# Counter({'e': 3, 'i': 2, 'G': 1, 'k': 1, ' ': 1, 'U': 1, 'n': 1, 'v': 1, 'r': 1, 's': 1, 't': 1, 'y': 1})
"""

# Realizando o import

from collections import Counter

# Exemplo 3

texto = """o nome do planeta-anão Plutão (imagem) foi sugerido inicialmente por Venetia Burney, na época uma 
menina de onze anos de idade?

… a maior fronteira territorial da França é com o Brasil, com 730 km de extensão?

… uma pedra fundamental da futura capital brasileira foi colocada no Morro do Centenário, Planaltina, em 1922, 
38 anos antes da inauguração de Brasília?

… após o lançamento do seu álbum Midnights, a artista estadunidense Taylor Swift se tornou a primeira pessoa da 
história a ocupar todas as posições do top 10 das paradas musicais Billboard Hot 100, Digital Songs e Streaming 
Songs, simultaneamente?

… o verbo japonês Busshu-suru, que significa vomitar, tem origem em um incidente em que o então presidente dos 
Estados Unidos George H. W. Bush regurgitou sobre o colo de Kiichi Miyazawa, então primeiro-ministro do Japão?"""

palavras = texto.split()

# print(palavras)

res = Counter(palavras)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))
