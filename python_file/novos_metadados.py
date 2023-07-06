import os  # pacote de integração com o sistema operacional.
from importlib import metadata

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

print(metadata.version('pip'))
print()

metadado_pip = metadata.metadata('pip')

print(list(metadado_pip))
print()

print(metadado_pip['Project-URL'])
print(len(metadado_pip))
print(metadata.requires('pip'))
print()
