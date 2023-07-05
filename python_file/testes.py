"""
# Execução dos testes com unittest
python ./python_file/testes.py

# Execução dos testes com unittest no modo verbose
python ./python_file/testes.py -v
"""
import os  # pacote de integração com o sistema operacional.
import unittest

from atividades import comer, dormir, eh_engracada

# limpando a tela do terminal, or None é para evitar a exibição de retorno
# do comando.
os.system('cls') or None


class AtividadesTetes(unittest.TestCase):
    def test_comer_saudavel(self):
        """Testando o retorno com comida saudável.
        """
        self.assertEqual(comer('quiabo', True),
                         'Estou comendo quiabo porque quero manter a forma.')

    def test_comer_gostosa(self):
        """Testando o retorno com comida gostosa.
        """
        self.assertEqual(comer(comida='pizza', eh_saudavel=False),
                         'Estou comendo pizza porque a gente só vive uma vez.')

    def test_dormir_pouco(self):
        """Testando o retorno dormindo puco.
        """
        self.assertEqual(
            dormir(4), 'Continuo cansado apás dormir por 4 horas. :(')

    def test_dormir_muito(self):
        """Testando o retorno dormindo muito.
        """
        self.assertEqual(
            dormir(10), 'Ptz! Dormir muito! Estou atrasado para o trabalho!')

    def test_eh_engracada(self):
        """Testando o retorno de é engraçada.
        """
        # self.assertEqual(eh_engracada("Sérgio Malandro"), False)
        self.assertFalse(eh_engracada("Sérgio Malandro"))
        self.assertTrue(eh_engracada("Jim Carrey"),
                        'Jim Carrey deveria ser engraçado.')


if __name__ == '__main__':
    unittest.main()
