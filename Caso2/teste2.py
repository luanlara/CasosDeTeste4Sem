import unittest
from codigoTestado2 import *

class TesteLimparPreco(unittest.TestCase):

    def testeErrado(self):
        objeto = 'R$ 99,999'
        desejado = 94.999
        real = CodigoTestado2.limparPreco(objeto)
        msg = "\nErro! \nResultado esperado é " + str(desejado) + " ≠ " + str(real)
        self.assertNotEqual(desejado, real, msg)
    
    def testeCerto(self):
        objeto = 'R$ 99,999'
        desejado = 99.999
        real = CodigoTestado2.limparPreco(objeto)
        msg = "\nErro! \nResultado esperado é " + str(desejado) + " \nValor real = " + str(real)
        self.assertEqual(desejado, real, msg)


if __name__ == '__main__':
    #run all test
    unittest.main() 
    

