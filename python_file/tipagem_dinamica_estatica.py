"""
Tipagem Dinâmica X Estática

Estática -> Uma linguagem é definida como estaticamente tipada quando a pessoa
que está programando precisa informar explicitamente o tipo de cada dado
utilizado no sistema: variáveis, parâmetros de funções, valores de retorno,
etc. Uma vez definido o tipo, estas variáveis estão restritas ao tipo
declarado; a checagem (type checking) é feita na compilação do programa ou em
tempo de execução (runtime), dependendo se a linguagem for compilada ou
interpretada.

Dinâmica -> O tipo é determinado (inferido) em runtime (ou tempo de execução)
de acordo com o valor do dado, e não a partir da variável. Nestes casos, o
programa observa qual é o tipo de cada dado que está sendo declarado do código
e, a partir disso, determina a tipagem. A sintaxe não exige que se informe
explicitamente o tipo quando definimos variáveis; em algumas linguagens é
possível informar explicitamente o tipo de dado, mas não é obrigatório.

idade = 42
print(type(idade))
print()
idade = 'Quarenta e dois'
print(type(idade))
print()



"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


if False:
    resultado = 1 + 'Geek'
else:
    resultado = 1 + 41

print(resultado)
print(type(resultado))
print()
