import unittest
import sys
sys.path.insert(1, '../modulos')
import modelos
import sistemas

"""
https://www.browserstack.com/guide/unit-testing-python
https://www.browserstack.com/guide/unit-testing-python
https://www.pythonclear.com/unittest/python-unittest-assertraises/
https://www.pythonclear.com/unittest/python-unittest-assertraises/
https://pypi.org/project/vectormath/
https://pypi.org/project/vectormath/
"""


class SistemaTestCase(unittest.TestCase):
	def test_p(self):
		populacao = modelos.Populacao(5000)
		sistema = sistemas.Sistema(populacao)

		self.assertEqual(sistema.p(5), 3)
		
	# def test_deslocamento_c(self):
    #     with self.assertRaises(TypeError):
    #         mecanica.deslocamento("2","5")


