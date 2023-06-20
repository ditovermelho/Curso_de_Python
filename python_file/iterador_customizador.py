"""
Escrevendo um iterador customizado


"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class Contador:
    def __init__(self, menor, maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):
        return self

    def __next__(self):
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor+1
            return numero
        raise StopIteration


for n in Contador(1, 61):
    print(n)

print()
for n in range(1, 61):
    print(n)

print()
