import math
import os  # pacote de integração com o sistema operacional.
import statistics

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# math.prod - retorna o produto de um container numérico
nuns_v1 = [2, 3, 6, 8]
nuns_v2 = (2, 3, 6, 8)
nuns_v3 = {2, 3, 6, 8}

print(math.prod(nuns_v1))  # 2 * 3 * 6 *8 -> 288
print(math.prod(nuns_v2))
print(math.prod(nuns_v3))
print()

# math.isqrt - retorna a parte inteira da raiz quadrada de um número
print(math.isqrt(9))
print(math.sqrt(9))
print(math.isqrt(17))
print(math.sqrt(17))
print()

# math.dist - retorna a distância euclidiana entre dois pontos, 3D ou 2D

# Pontos 3D
p3d1 = (12, 50, 40)
p3d2 = (6, 7, 13)

# Pontos 2D
p2d1 = [12, 50]
p2d2 = [6, 7]

print(math.dist(p3d1, p3d2))
print(math.dist(p2d1, p2d2))
print()

# math.hypot - retorna a hipotenusa, ou norma Euclidiana
print(math.hypot(*p3d1))
print(math.hypot(*p2d1))
print()

# Estatística

# statistics.fmean - calcula a média de números reais

valores_reais = [1.45, 6.789, 3.45, 89.98765]
valores_interiros = [1, 6, 3, 89]

print(statistics.fmean(valores_reais))
print(statistics.fmean(valores_interiros))
print()

# statistics.geometric_mean - calcula a média geométrica de números rais.
print(statistics.geometric_mean(valores_reais))
print(statistics.geometric_mean(valores_interiros))
print()

# statistics.multimode - retorna o valor mais frequente em uma sequência.
seq1 = 'Geek University'
seq2 = [3, 5, 3, 8, 7, 9, 5, 3]
seq3 = [1, 2, 3, 1, 2, 3, 4, 5, 6]

print(statistics.multimode(seq1))
print(statistics.multimode(seq2))
print(statistics.multimode(seq3))
print()
