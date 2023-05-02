""" 
Módulo Collections - Default Dict

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podemos utilizar um lambda para isso. Este valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será attribuido.

# Recap Dicionários

dicionario = {'curso': 'Progamação em Python: Essencial'}

print(dicionario)

print(dicionario['curso'])

print(dicionario['outro']) # ??? keyError

OBS: Lambdas são funções sem nome, que podem ou não receber parâmentros de entrada
e retornar valores.
"""

# Fazendo import

from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Progamação em Python: Essencial'

print(dicionario)

print(dicionario['outro'])  # KeyError no dicionário comum, mas aqui não;

print(dicionario)
