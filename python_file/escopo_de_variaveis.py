"""
Escopo de variáveis

Dois casos de escopo:

1 - Variáveis globais;
     - Variáveis globais são reconhecidas, ou seja, seu escopo compreende, todo o o progama.
2 - Variáveis locais;
     - Variáveis locais são reconhecidas apenas no bloco onde foram declaradas, ou seja, seu escopo
     esta limitado ao bloco onde foi declarado.

Para declarar variáves em Python fazemos:

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinânima. Isso significa que ao declararmos uma variável, nós não colocamos
o tipo de dado dela. Este tipo é inferido ao atribuírmos o valor à mesma.

Exemplo em C:
int numero = 42;

Exemplo em Java:
int numero = 42;
"""

numero = 42
print(numero)
print(type(numero))

if numero > 10:
    novo = numero +10 # A variavel 'novo' esta declarada localmente dentro do bloco if.
    print(novo)

print(novo)