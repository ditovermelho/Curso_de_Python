"""
Módulos Customizados

Como módulos Python nada mais são do que arquivos Python, então Todos os
arquivos que criamos neste curso são módulos Python para serem utilizados.


from funcoes_com_parametro import soma_impares

print(soma_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print()

# Importando todo módulo (Temos acesso a TODOS os elementos do módulo)
import funcoes_com_parametro as fcp

# Estamos acessando e imprimindo uma variável contida no módulo
print(fcp.lista)
print()
print(fcp.tupla)
print()
print(fcp.soma_impares(fcp.lista))
print()

"""
import os  # pacote de integração com o sistema operacional.

from map import c_para_f, cidades

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

print(list(map(c_para_f, cidades)))
print()
