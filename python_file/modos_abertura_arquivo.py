"""
Modos de Abertura de Arquivo

r -> Abre para leitura - padrão
w -> Abre para escrita - sobrescreve caso o arquivo já exista.
x -> Abre para escrita somente se o arquivo não existir.
a -> Abre para escrita, adicionando o conteúdo ao final do arquivo.
+ -> Abre para o modo de atualização: leitura e escrita. (Temos o controle do
cursor)

# OBS: Abrindo no modo 'a' -> append, se o arquivo não existir será criado.
Caso exista, o novo conteúdo será SEMPRE adicionado ao final. Com o modo 'a',
não controlamos o cursor.


https://docs.python.org/3/library/functions.html#open

# Exemplo x:
try:
    with open('./python_file/university.txt', 'x', encoding='UTF-8') as arquivo:
        arquivo.write('Teste de comando 2.\n')
except FileExistsError:
    print('Arquivo já existe')


# Exemplo a:

with open('./python_file/frutas.txt', 'a', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + '\n')
        else:
            break


"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

with open('./python_file/outro.txt', 'a+', encoding='UTF-8') as arquivo:
    arquivo.write('Adicionada.\n')
    arquivo.write('Nova linha.\n')
    arquivo.write('Mais uma linha.\n')
