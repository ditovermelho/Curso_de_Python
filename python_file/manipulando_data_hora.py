"""
Manipulando Data Hora

Python tem um módulo built-in (integrado) para se trabalhar com data e hora
chamado datetime

print(dir(datetime))
print()
print(datetime.MAXYEAR)
print(datetime.MINYEAR)
print()
# Retorna a data e hora corrente
print(datetime.datetime.now())  # 2023-07-02 20:37:14.213418
print()
# datetime.datetime(year, month, day, hour, minute, second, microsecond)
print(repr(datetime.datetime.now()))
print()
# replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)
print()
# Alterar o horário para 16 horas, 0 minuto, 0 segundo, 0 microsegundo
inicio = inicio.replace(year=2023, hour=16, minute=0, second=0, microsecond=0)
print(inicio)
print()

# Recebendo dados dos usuários e convertendo para data 
evento = datetime.datetime(2019, 1, 1, 0)
print(type(evento))
print(type('31/12/2018'))
print(evento)
print()

nascimento = input('Informe sua data de nascimento (dd/mm/yyyy): ')
nascimento = nascimento.split('/')
nascimento = datetime.datetime(
    int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))
print(nascimento)
print(type(nascimento))
print()

"""
import datetime
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

evento = datetime.datetime.now()
# Acesso individual dos elementos de data e hora
print(evento.year)  # ano
print(evento.month)  # mês
print(evento.day)  # dia
print(evento.hour)  # hora
print(evento.minute)  # minuto
print(evento.second)  # segundo
print(evento.microsecond)  # microsegundo
print()
