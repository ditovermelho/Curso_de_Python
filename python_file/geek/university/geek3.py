from geek import geek2


def funcao():
    return 'Geek'


def funcao2():
    geek2.funcao1()


if __name__ == "__maim__":
    funcao2()
    print("geek3.py está sendo executado diretamente")
else:
    print(f'geek3.py foi importado - {__name__}')
