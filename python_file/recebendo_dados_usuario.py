"""
Recebendo dados do usuário

input() -> Todo dado recebido via input é do tipo String
- Aspas simpes;
- Aspas duplas;
- Aspas simples triplas;
- Aspas duplas triplas;

Exemplos:
- Aspas simpes -> 'geek'
- Aspas duplas -> "geek"
- Aspas simples triplas -> '''geek'''
"""
#- Aspas duplas triplas -> """geek"""

# Entrada de daos
# print("Qual seu nome? ")
# nome = input() # input = Entrada

nome = input('Qual seu nome? ')

# Exemplo de print "antigo" 2.x
# print('Seja bem-vindo(a) %s' % nome.title())

# Exemplo de print "moderno" 3.x
# print('Seja bem-vindo(a) {0}'.format(nome.title()))

# Exemplo de print 'Mais atual?' 3.7
print(f"Seja bem-vindo(a) {nome.title()}")

# print("Qual sua idade? ")
# idade = input()

idade = int(input('Qual sua idade? '))

# Processamento

# Saida de dados
# Exemplo de print "antigo" 2.x
# print('%s tem %s anos' % (nome.title(), idade))

# Exemplo de print "moderno" 3.x
# print('{0} tem {1} anos'.format(nome.title(), idade))

# Exemplo de print 'Mais atual?' 3.7
print(f"{nome.title()} tem {idade} anos")

"""
# int(idade) => cast

Cast é a 'conversão' de um tipo de dado para outro.
"""

print(f"{nome.title()} naceu em {2023 - idade}")