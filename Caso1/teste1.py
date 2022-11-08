import unittest
from codigoTestado1 import *

class TesteRaspagem(unittest.TestCase):
    def teste(self):
        driver = webdriver.Chrome()

        paguemenos = CodigoTestado1.coletar_paguemenos(driver)
        print(paguemenos)

        driver.close()

        self.assertEqual(len(paguemenos), 15, "Erro na lista")
        contador = 0
        for medicamento in paguemenos:
            self.assertNotEqual(medicamento['preco'], -1, "Problema no preco")
            contador += 1
        self.assertGreaterEqual(contador, 15, "Lista menor que o esperado")

if __name__ == '__main__':
    #run all test
    unittest.main() 
    

