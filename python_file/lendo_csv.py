"""
Lendo arquivos CSV

CSV - Comma Separeted Values - Valores Separados por Vírgula

# Separador por vírgula
1, 2, 3, 4, 5, 6

"geek", "university", 'python', 'ciência', 'dados'

# Separador por ponte e vírgula
1; 2; 3; 4; 5; 6

"geek"; "university"; 'python'; 'ciência'; 'dados'

# Separador por espaço
1 2 3 4 5 6

"geek" "university" 'python' 'ciência' 'dados'

http://dados.gov.br/dataset

# Possível de se trabalhar, mas não é o ideal (trabalhoso)
with open('./data/lutadores.csv', encoding='UTF-8') as arquivo:
    dados = arquivo.read()
    print(type(dados))
    dados = dados.split(',')
    print(dados)

A linguagem Python possui duas formas diferente para ler dados em arquivos CSV:
    - reader -> Permite que iteremos sobre as linhas do arquivos csv como
    listas;
    - DictReader -> Permite que iteremos sobre as linhas do arquivo CSV como
    OrderedDicts;

# Reader
from csv import reader

with open('./data/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = reader(arquivo)
    next(leitor_csv) # Pula o cabeçalho
    for linha in leitor_csv:
        # Cada linha é uma lista
        print(f'{linha[0]} nasceu em {linha[1]} e mede {linha[2]} centímetros')

# DictReader
from csv import DictReader

with open('./data/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo)
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")

# DictReader com outo separador

"""
import os  # pacote de integração com o sistema operacional.
from csv import DictReader

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

with open('./data/lutadores.csv', encoding='UTF-8') as arquivo:
    leitor_csv = DictReader(arquivo, delimiter=',')
    for linha in leitor_csv:
        # Cada linha é um OrderedDict
        print(
            f"{linha['Nome']} nasceu no(a)(s) {linha['País']} e mede {linha['Altura (em cm)']}")
