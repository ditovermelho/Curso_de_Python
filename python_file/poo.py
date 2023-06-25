"""
Programação Orientada a Objetos - POO

- POO é um paradigma de programação que utiliza que mapeamento de objetos do
mundo real para modelos computacionais.

- Paradigma de programação é a forma/metodologia utilizada para pensar/
desenvolver sistemas.

Principais elementos da Orientação a Objetos:
- Classe -> Modelo do objeto do mundo real sendo representado
computacionalmente.
- Atributo -> Características do objeto.
- Método -> Comportamento do objeto (funções).
- Construtor -> Método especial utilizado para criar os objetos.
- Objeto -> Instância da classe.

"""
import os  # pacote de integração com o sistema operacional.

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None

numero = 10
print(numero)
print(type(numero))
print()
nome = 'Geek'
print(nome)
print(type(nome))
print()


class Produto:
    pass


ps4 = Produto()
print(ps4)
print(type(ps4))
print()
