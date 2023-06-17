"""
Escrever em arquivos

# OBS: Ao abrir um arquivo para leitura, não podemos realizar a escrita nele.
Apenas ler. Da mesma forma, se abrir um arquivo para escrita, não podemos
lê-lo, somente escrever nele.

# OBS: Ao abrir um arquivo para escrita, o arquivo é criado no sistema
operacional.

Para escrevermos dados em um arquivos, após abrir o arquivo utilizamos a função
write(). Esta função recebe uma string como parâmetro, caso contrario teremos
um TypeError.

Abrindo um arquivo para escrita com o modo 'w', se arquivo não existir será
criado, caso ele já exista, o anterior será apagado e um novo será criado.
Dessa forma, todo o conteúdo no arquivo anterior é perdido.

# Exemplo de escrita - modo 'w' - write (escrita)

# Forma tradicional de escrita em arquivo (Não Pythônica)
arquivo = open('mais.txt', 'w')
arquivo.write('Um texto qualquer.\n')
arquivo.write('Mais um texto.')
arquivo.close()

# Forma Pythônica:

with open('./python_file/novo.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Escrever dados em arquivo é muito fácil.\n')
    arquivo.write('Podemos colocar quantas linhas quisermos.\n')
    arquivo.write('Esta é a última linha')

with open('./python_file/geek.txt', 'w', encoding='UTF-8') as arquivo:
    arquivo.write('Geek' * 1000)
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

with open('./python_file/frutas.txt', 'w', encoding='UTF-8') as arquivo:
    while True:
        fruta = input('Informe uma fruta ou digite sair: ')
        if fruta != 'sair':
            arquivo.write(fruta + ' ')
        else:
            break
