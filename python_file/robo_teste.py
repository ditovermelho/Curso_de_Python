"""
python ./python_file/robo_teste.py -v
"""

import os  # pacote de integração com o sistema operacional.
import unittest

from robo import Robo

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class RoboTestes(unittest.TestCase):

    def setUp(self) -> None:
        print("\nSetUp() sendo executado")
        self.megaman = Robo('Mega Man', bateria=50)
        return super().setUp()

    def test_carregar(self):
        self.megaman.cargar_completa()
        self.assertEqual(self.megaman.bateria, 100)

    def test_dizer_nome(self):
        self.assertEqual(self.megaman.dizer_nome(),
                         'BEEP BOOP BEEP BOOP. EU SOU MEGA MAN')
        self.assertEqual(self.megaman.bateria, 49,
                         'A bateria deveria estar em 49%')

    def test_aprender_habilidade(self):
        pass

    def tearDown(self) -> None:
        print("TearDown() sendo executado")
        return super().tearDown()


if __name__ == '__main__':
    unittest.main()
