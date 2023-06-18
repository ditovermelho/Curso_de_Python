"""
StringIO

ATENÇÂO: Para ler ou escrever dados em arquivos do sistema operacional o
software precisa ter permissão:
    - Permissão de Leitura -> Para ler o arquivo.
    - Permissão de Escrita -> Para escrever o arquivo.

StringIO -> Utilizado para ler e criar arquivos em memória.
"""
import os  # pacote de integração com o sistema operacional.
# Primeiro fazemos o import
from io import StringIO

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


mensagem = 'Este é apenas uma string normal'

# Podemos criar um arquivo em memória já com uma string inserida ou mesmo vazio
# para inserirmos texto depois
arquivo = StringIO(mensagem)
# arquivo = open ('./python_file/arquivo.txt', 'w')

# Agora tendo o arquivo, podemos utilizar tudo que já sabemos
print(arquivo.read())
print()

# Escrevendo outros textos
arquivo.write('\nOutro texto\n')

# Podemos inclusive movimentar o cursor
arquivo.seek(0)

print(arquivo.read())
print()
