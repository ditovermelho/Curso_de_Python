"""
Sistema de Arquivos - Manipulação

# Descobrindo se um arquivo ou diretório existe
# Arquivo
print(os.path.exists('./python_file/arquivo.txt'))  # False
print()
print(os.path.exists('./python_file/frutas.txt'))  # True
print()

# Diretório
# Paths relativos
print(os.path.exists('./python_file/geek'))  # True
print()
print(os.path.exists('./python_file/geek/university'))  # True
print()
print(os.path.exists('./python_file/outro'))  # False
print()

# Paths absolutos
print(os.path.exists('/home/geek/university'))  # False
# True
print(os.path.exists('D:\carlos daniel\Documents\Python\Curso de Python'))

# Criando arquivos

# Forma 1
open('./python_file/arquivo-teste.txt', 'w').close()

# Forma 2
with open('./python_file/arquivo-teste2.txt', 'a') as arquivo:
    pass

os.mknod('./python_file/arquivo-teste3.txt') # Retorno de erro AttributeError

# OBS: Se você estiver utilizando Mac OS, pode gerar um erro de PermissionError
# OBS: Criando um arquivo vai mknod() se o arquivo já existir teremos o erro
FileExistsError

# Criando diretórios - únicos (um a um)

# Path Relativo
os.mkdir('./python_file/templates')

# Path Absoluto
os.mkdir(''D:\carlos daniel\Documents\Python\templates')

# OBS: A função mkdir cria um diretório se este não existir. Caso exista, temos
FileExistsError
# OBS: Se não tivermos a permissão para criar o diretório teremos um
PermissionError

# Criando multi-diretórios (arvores de diretórios)
os.makedirs('./python_file/templates/geek/university/outro')

# OBS: Se já existir, teremos um FileExistsError

os.makedirs('./python_file/templates2/novo2/outro2', exist_ok=True)

# Renomear arquivos e diretórios

# Diretório
os.rename('./python_file/templates2', './python_file/geek2')

# OBS: Se o diretório não existir teremos um FileExistsError
# OBS: Se o diretório que queremos renomear não estiver vazio,  teremos um
OSError

# Arquivo
os.rename('./python_file/arquivo-teste2.txt', './python_file/arquivo.txt')

# Atenção! Tome cuidado com os comandos de deleção. Ao deletarmos um arquivo ou
diretório, eles não vão para lixeira. Eles são apagados permanente.

# Removendo arquivos
os.remove('./python_file/arquivo-teste.txt')

# OBS: Se você estiver no Windows e o arquivo que você for deletar estiver em
uso, você terá um erro.

# OBS: Caso o arquivo não exista, teremos o FileNotFoundError

# OBS: Se você informar um diretório ao invés de um arquivo, teremos um
IsADirectoryError.

# Removendo diretórios vazios

os.rmdir('./python_file/templates')

# OBS: Se o diretório tiver qualquer conteúdo teremos um OSError
# OBS: Se o diretório não existir teremos um FileNotFoundError

# Removendo uma árvore de diretórios
for arquivo in os.scandir('./python_file/geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)
    if not arquivo.is_file():
        os.rmdir(arquivo.path)

# Podemos remover uma arvore de diretórios vazios
os.removedirs('./python_file/geek2/novo2/outro2')

# OBS: Se algum dos diretórios contiver arquivos ou outros diretórios, o
processo para.

# Atenção: Ao remover arquivos e diretórios com Python eles não vão para
lixeira. Eles vaõ embora!

# Instalando modulo lixeira
pip install send2trash

# Importando a biblioteca send2trash
from send2trash import send2trash

# Não vai para lixeira. É deletado imediatamente
os.remove('./python_file/frutas2.txt')

# Vai para lixeira. Pode ser restaurado.
send2trash('./python_file/frutas.txt')

# OBS: Se o arquivo não existir, teremos OSError

# Trabalhando com arquivos e diretórios temporários
import tempfile

# Criando um diretório temporário
with tempfile.TemporaryDirectory() as tmp:
    print(f'Criei o diretório temporário em {tmp}')
    with open(os.path.join(tmp, 'arquivo_temporario.txt'), 'w') as arquivo:
        arquivo.write('Geek University\n')
    input()

# Estamos criando um diretório temporário, abrindo o mesmo e dentro dele
# criando um arquivo para escrevermos um texto. No final usamos um input() só
# para mantermos os arquivos temporários 'vivos' dentro dos blocos with.

# OBS: possivelmente, o código acima não irá funcionar se você estiver usando
# o Windows. Por conta desse sistema trabalhar de forma diferente com arquivos
# temporários.

# Criando um arquivo temporário

with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n')
    tmp.seek(0)
    print(tmp.read())

# OBS: Em arquivos temporários só conseguimos escrever bits. Por isso,
# utilizamos b''

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None
