"""
Métodos de Data e Hora

#  Com now() podemos especificar um timezone (Fuso Horário)
agora = datetime.datetime.now()  # now == agora
print(agora)
print(type(agora))
print(repr(agora))
print()

hoje = datetime.datetime.today()  # today == hoje
print(hoje)
print(type(hoje))
print(repr(hoje))
print()

# Mudanças ocorrendo à meia-noite combine()
manutencao = datetime.datetime.combine(
    (datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))
print()

# Encontrar o dia da semana. weekday()

Os dias da semana do método weekday() começam em 0, sendo esta a segunda-feita
0 - Segunda-feira (Monday)
1 - Terça-feira (Tuesday)
2 - Quanta-feira (Wednesday)
3 - Quinta-feira (Thursday)
4 - Sexta-feira (Friday)
5 - Sábado (Saturday)
6 - Domingo (Sunday)

print(manutencao.weekday())
print()

aniversario = input('Qual e a sua data de nascimento? dd/mm/yyyy: ')
aniversario = aniversario.split('/')
aniversario = datetime.datetime(
    year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

# Forma trabanhosa
if aniversario.weekday() == 0:
    print('Você nasceu em uma Segunda-feira')
elif aniversario.weekday() == 1:
    print('Você nasceu em uma Terça-feira')
elif aniversario.weekday() == 2:
    print('Você nasceu em uma Quanta-feira')
elif aniversario.weekday() == 3:
    print('Você nasceu em uma Quinta-feira')
elif aniversario.weekday() == 4:
    print('Você nasceu em uma Sexta-feira')
elif aniversario.weekday() == 5:
    print('Você nasceu em um Sábado')
elif aniversario.weekday() == 6:
    print('Você nasceu em um Domingo')
dia_semana = {0: 'Segunda-feira', 1: 'Terça-feira', 2: 'Quanta-feira',
              3: 'Quinta-feira', 4: 'Terça-feira', 5: 'Sábado', 6: 'Domingo'}

# Forma menos trabalhosa
dia = aniversario.weekday()
print(f'Você nasceu em um(a) {dia_semana[dia]}')
print()

# Forma 1
def formata_data(data):
    mes = {1: 'Janeiro', 2: 'Fevereiro', 3: 'Março', 4: 'Abril', 5: 'Maio',
           6: 'Junho', 7: 'Julho', 8: 'Agosto', 9: 'Setembro', 10: 'Outubro',
           11: 'Novembro', 12: 'Dezembro'}
    return f"{data.day} de {mes[data.month]} de {data.year}"

# Forma 2 - Requer conexão com a Internet
from textblob import TextBlob

def formata_data(data):
    return f"{data.day} de {TextBlob(data.strftime('%B')).translate(from_lang='en', to='pt-br')} de {data.year}"

# Formatando datas/horas com strftime() (String Format Time)
# dd/mm/yyyy hora:minuto

hoje = datetime.datetime.today()
print(hoje)
hoje_formatado = hoje.strftime('%d/%m/%Y')
print(hoje_formatado)
print(formata_data(hoje))
print()

nascimento = datetime.datetime.strptime('10/04/1998', '%d/%m/%Y')
print(nascimento)
print()

nascimento = input('Qual e a sua data de nascimento? dd/mm/yyyy: ')
nascimento = datetime.datetime.strptime(nascimento, '%d/%m/%Y')
print(nascimento)
print()

import timeit

# Somente a Hora

almoco = datetime.time(12, 30, 0)
print(almoco)
print()

# Marcando tempo de execução do nosso código com timeit

# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print(tempo)
print()

# List Comphension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])', number=10000)
print(tempo)
print()

# Map
tempo = timeit.timeit(
    '"-".join(map(str, range(100)))', number=10000)
print(tempo)
print()
"""
import functools
import os  # pacote de integração com o sistema operacional.
import timeit

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def teste(n):
    soma = 0
    for num in range(n * 200):
        soma = soma + num ** num + 4
    return soma


print(timeit.timeit(functools.partial(teste, 2), number=10000))
print()
