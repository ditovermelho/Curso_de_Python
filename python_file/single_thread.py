"""
Single Thread

"""
import os  # pacote de integração com o sistema operacional.
import time

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

CONTADOR = 50000000


def contagem_regressiva(n):
    while n > 0:
        n -= 1


inicio = time.time()
contagem_regressiva(CONTADOR)
fim = time.time()

print(f'Tempo em segundos: {fim - inicio}')
# Tempo em segundos: 10.934999465942383
