curso = 'Programação em Python: Essencial'


def qual_curso():
    return curso


def funcao1():
    print('Geek University - geek2.py')


if __name__ == '__main__':
    funcao1()
    print("geek2.py está sendo executado diretamente")
else:
    print(f'geek2.py foi importado - {__name__}')
