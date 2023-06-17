"""
SeeK e Cursors

seek() -> É utilizado para movimentar o cursor pelo arquivo.

arquivo = open('./python_file/texto.txt', encoding='UTF-8')

print(arquivo.read())
print()

# Movimentando o cursor pelo arquivo com a função seek()
arquivo.seek(0)

print(arquivo.read())
print()

arquivo.seek(21)

print(arquivo.read())
print()

# readline() -> Função que lé linha a linha

ret = arquivo.readline()

print(type(ret))
print(ret)
print(ret.split(' '))
print()

# readlines()

linhas = arquivo.readlines()

print(len(linhas))
print()

OBS: Quando abrimos um arquivo com a função open() é criada uma conexão entre o
arquivo no disco do computador e o nosso programa. Essa conexão é chamada de
streaming. Ao finalizar os trabalhos com o arquivo devemos fechar essa conexão.
Para isso utilizamos a função close()

Passos para se trabalhar com um arquivo:

1 - Abrir o arquivo;
2 - Trabalhar o arquivo;
3 - Fechar o arquivo;

# 1 - Abrir o arquivo:
arquivo = open('./python_file/texto.txt', encoding='UTF-8')

# 2 - Trabalhar o arquivo:
print(arquivo.read())
print()

# 3 - fechar o arquivo:
arquivo.close()

print(arquivo.close) # True - Verifica se o arquivo está aberto ou fechado
print()

# OBS: Se tentarmos manipular o arquivo após seu fechamento, teremos um 
ValueError
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

arquivo = open('./python_file/texto.txt', encoding='UTF-8')

# Com a função read() podemos limitar a quantidade de caracteres a serem lidos
# no arquivo
print(arquivo.read(50))
