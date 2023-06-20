"""
Criando sua própria versão do loop


for num in [1, 2, 3, 4, 5]:
    print(num)

for letra in 'Geek University':
    print(letra)

iter([1, 2, 3, 4, 5])

iter('Geek University')

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


def meu_for(interavel):
    it = iter(interavel)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


meu_for('Geek University')

numeros = [1, 2, 3, 4, 5]

meu_for(numeros)
