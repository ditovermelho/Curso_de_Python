"""
Unittest - Antes e após hooks

-----
hooks - são os testes em si. Ou seja, a execução dos testes.
-----

setup() -> é executado antes de cada teste. É util para criarmos instâncias de
objetos e outros dados;

tearDow() -> é executado ao final de cada método de teste. É util para excluir
dados ou fechar conexões com o banco de dados.


"""
import os  # pacote de integração com o sistema operacional.
import unittest

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class ModuloTest(unittest.TestCase):
    def setup(self):
        """Configuração do setUp()
        """
        pass

    def test_primeiro(self):
        """setup vai rodar antes do teste
        tearDown() vai rodar após o teste.
        """
        pass

    def test_segundo(self):
        """setup vai rodar antes do teste
        tearDown() vai rodar após o teste.
        """
        pass

    def tearDown(self):
        """Configurações do tearDown()
        """
        pass
