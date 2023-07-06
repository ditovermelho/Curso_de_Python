import os  # pacote de integração com o sistema operacional.

from models.calcular import Calcular

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

calc: Calcular = Calcular(1)

print(calc)
