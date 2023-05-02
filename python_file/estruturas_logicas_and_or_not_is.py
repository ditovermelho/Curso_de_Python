"""
Estruturas lógicas: and (e), or (ou), not (não), is (é)

Operadores unários:
    - not, is
Operadores binários:
    - and, or

Para o 'and', ambos os valores precisam ser True
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True

"""

ativo = True
logado = False

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor, chequer seu e-mail") 

if not ativo:
    print("Você precisa ativar sua conta. Por favor, chequer seu e-mail")
else: 
    print("Bem-vindo usuário!")

if ativo is False:
    print("Você precisa ativar sua conta. Por favor, chequer seu e-mail")
else:
    print("Bem-vindo usuário!")
