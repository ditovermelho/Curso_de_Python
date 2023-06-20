"""
Geradores

- Geradores (Generators) são Iterators (Iteradores);

OBS: O contrario não é verdadeiro. Ou seja, nem todo iterator é um generator

Outras informações:
- Generators podem ser criados com funções geradores;
- Funções geradoras utilizam a palavra reservada yield;
- Generators podem ser criados com Expressões Geradoras;

Diferenças entre funções e Generator Functions (Funções Geradoras)

-------------------------------------------------------------------------------
| Funções                            | Generator Functions                    |
-------------------------------------------------------------------------------
| Utilizam Return                    | Utilizam yield                         |
-------------------------------------------------------------------------------
| Retorna uma vez                    | Podem utilizar yield múltiplas vezes   |
-------------------------------------------------------------------------------
| Quando executada, retorna um valor | Quando executada, retorna um generator |
-------------------------------------------------------------------------------

gen = conta_ate(5)

print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print()

gen = conta_ate(10)

for num in gen:
    print(num)

print()
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Exemplo Generator Function


def conta_ate(valor_maximo):
    contador = 1
    while contador <= valor_maximo:
        yield contador
        contador += 1

# OBS: Uma Generator Function não é um Generator. Ela gera um generator. ok?


gen = list(conta_ate(10))

print(gen)
print()
