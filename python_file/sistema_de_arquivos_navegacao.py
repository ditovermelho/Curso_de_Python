"""
Sistema de Arquivos e Navegação

Para fazer uso de manipulação de arquivo do sistema operacional, precisamos
importar e fazer uso do módulo os.

os -> Operating System - Sistema Operacional

# getcwd() -> pega o current work directory - diretório de trabalho corrente
# Retorna o path (caminho) absoluto
print(os.getcwd())  # D:\carlos daniel\Documents\Python\Curso de Python
print()

# Para mudar o diretório, podemos utilizar o chdir()

os.chdir('..')

print(os.getcwd())  # D:\carlos daniel\Documents\Python
print()

os.chdir('..')

print(os.getcwd())  # D:\carlos daniel\Documents
print()

os.chdir('..')

print(os.getcwd())  # D:\carlos daniel
print()

os.chdir('..')

print(os.getcwd())  # D:
print()

os.chdir('..')

print(os.getcwd())  # ??
print()

# Podemos checar se um diretório é absoluto ou relativo

print(os.path.isabs('D:\carlos daniel')) # True
print()

# OBS: para usuários Windows
# Se você, infelizmente, estiver utilizando um computador com Windows.
# terá que ter cuidado ao verificar diretórios.

print(os.path.isabs('C:\\carlos daniel'))

# Podemos identificar o sistema operacional com modulo os
print(os.name)  # posix (Linux e Mac), nt (Windows)
print()

import sys

# Podemos ter mais detalhes no sistema operacional
# Comando para Linux: print(os.uname())
print(sys.platform)  # Para windows
print()

# 'D:\carlos daniel\workspace\system'

print(os.getcwd())  # D:\carlos daniel\Documents\Python\Curso de Python
print()

res = os.path.join(os.getcwd(), 'python_file')

os.chdir(res)

print(os.getcwd())
print()

# Veja que o os.path.join() recebe dois parâmetros, sendo o primeiro o
# diretório atual e o segundo o diretório que será juntado ao atual.  

# Podemos listar os arquivos e diretórios com o listdir()

print(len(os.listdir('C://')))
print()

# Podemos listar os arquivos e diretórios com mais detalhes com scandir()

# Forma tradicional;

scanner = os.scandir()

arquivos = list(scanner)

print(arquivos)
print()
print(dir(arquivos[0]))
print()
print(arquivos[0].inode())  # ??
print()
print(arquivos[0].is_dir())  # É um diretório? True
print()
print(arquivos[0].is_file())  # É um arquivo? False
print()
print(arquivos[0].is_symlink())  # É um link simbólico? False
print()
print(arquivos[0].name)  # Nome do arquivo
print()
print(arquivos[0].path)  # Caminho até o arquivo
print()
print(arquivos[0].stat())  # Estatísticas...
print()

# OBS: Quando utilizarmos a função scandir() nós precisamos fechá-la, assim
# quando abrimos um arquivo.

scanner.close()


"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

# Forma pytônica

with os.scandir() as scanner:
    arquivos = list(scanner)
    scanner.close()

print(arquivos)
print()
print(dir(arquivos[0]))
print()
print(arquivos[0].inode())  # ??
print()
print(arquivos[0].is_dir())  # É um diretório? True
print()
print(arquivos[0].is_file())  # É um arquivo? False
print()
print(arquivos[0].is_symlink())  # É um link simbólico? False
print()
print(arquivos[0].name)  # Nome do arquivo
print()
print(arquivos[0].path)  # Caminho até o arquivo
print()
print(arquivos[0].stat())  # Estatísticas...
print()
