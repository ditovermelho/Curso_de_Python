import os  # pacote de integração com o sistema operacional.

from models.cliente import Cliente
from models.conta import Conta

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

felicity: Cliente = Cliente(
    'Felicity Jones', 'felicity@gmail.com', '123.456.789-01', '02/09/1987')
angelina: Cliente = Cliente(
    'Angelina Jolie', 'angelina@gmail.com', '234.567.890-02', '08/07/1978')

print(felicity)
print()
print(angelina)
print()

contaf: Conta = Conta(felicity)
contaa: Conta = Conta(angelina)

print(contaf)
print()
print(contaa)
print()
