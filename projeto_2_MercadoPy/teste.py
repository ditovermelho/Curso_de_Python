import os  # pacote de integração com o sistema operacional.

from models.produto import Produto

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

ps4 = Produto("Playstation 4", 1789.44)
xbox = Produto('Xbox 360', 1699.00)

print(ps4)
print()
print(xbox)
print()
