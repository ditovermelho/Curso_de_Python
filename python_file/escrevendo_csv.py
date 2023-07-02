"""
Escrevendo em arquivos CSV

reader() (leitor),  writer() (escritor)

writerow() -> Escreve uma linha
writer() -> Gera um objeto para que possamos escrever em um arquivo CSV.
Utilizamos o método writerow() para escrever cada linha. Este método recebe uma
lista.

# writer
from csv import writer

with open('./data/filmes.csv', 'a', encoding='UTF-8') as arquivo:
    escritor_csv = writer(arquivo)
    filme = None
    escritor_csv.writerow(['Título', 'Gênero', 'Duração'])
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow([filme, genero, duracao])

# DictWriter
from csv import DictWriter


"""
import os  # pacote de integração com o sistema operacional.
from csv import DictWriter

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

with open('./data/filmes.csv', 'a', encoding='UTF-8') as arquivo:
    cabecalho = ['Título', 'Gênero', 'Duração']
    escritor_csv = DictWriter(arquivo, fieldnames=cabecalho)
    escritor_csv.writeheader()
    filme = None
    while filme != 'sair':
        filme = input('Informe o nome do filme: ')
        if filme != 'sair':
            genero = input('Informe o gênero: ')
            duracao = input('Informe a duração (em minutos): ')
            escritor_csv.writerow(
                {"Título": filme, "Gênero": genero, "Duração": duracao})
