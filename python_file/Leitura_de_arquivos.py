"""
Leitura de Arquivos

Para o conteúdo de um arquivo em Python, utilizamos a função integrada open()
que literalmente significa 'abrir'.

open() -> Na forma mais simples de utilização nós passamos apenas um parâmetro
de entrada, que neste caso é o caminho para o arquivo a ser lido. Essa função
retorna um _io. TextIOWrapper e é com ele que trabalhamos então.

https://docs.python.org/3/library/functions.html#open

# OBS: Por padrão, a função open() abre o arquivo para leitura. Este arquivo
deve existir, ou então teremos o erro FileNotFoundError

<_io.TextIOWrapper name='./python_file/texto.txt' mode='r' encoding='UTF-8'>

mode r -> Modo de leitura. r -> read() -> ler
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Exemplo

arquivo = open('./python_file/texto.txt', encoding='UTF-8')

print(arquivo)
print(type(arquivo))
print()

# print(arquivo.read())
res = arquivo.read()
print(res)
print(type(res))
print()

# OBS: O Python, utiliza um recuso para trabalhar com arquivos chamado cursor.
# Esse cursor, funciona como o cursor quando estamos escrevendo.

# OBS: A função read() lê todo o conteúdo do arquivo.
