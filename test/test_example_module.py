"""Esse arquivo testa o arquivo example_module.py"""

import unittest  # para criar o caso de teste
from example_module import soma, multiplicação


class TestExampleModule(unittest.TestCase):
    """Classe que testa o arquivo example_module.py"""

    def test_soma(self):
        """
        Testa se a função de soma retorna o valor correto 5 quando chamada com 2 e 3
        """
        self.assertEqual(5, soma(2, 3))

    def test_multiplicação(self):
        """
        Testa se a função de multiplicação retorna o valor correto 6
        quando chamada com 2 e 3
        """
        self.assertEqual(6, multiplicação(2, 3))
