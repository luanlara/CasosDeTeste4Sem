import unittest
from codigoTestado3 import *

engine = create_engine('mysql+mysqlconnector://root:root@localhost/farmaticos')

class TesteRaspagem(unittest.TestCase):
    def teste(self):
        driver = webdriver.Chrome()

        paguemenos = CodigoTestado3.coletar_paguemenos(driver)
        print(paguemenos)

        driver.close()
    
        with Session(engine) as sessao, sessao.begin():
            registros = sessao.execute(text("SELECT idpreco, preco FROM preco"))
            inicio = len(list(registros))
            print(inicio)
            CodigoTestado3.registrarDados(paguemenos, sessao)

        registros = sessao.execute(text("SELECT idpreco, preco FROM preco"))
        sessao.close()

        registros = list(registros)
        engine.dispose()
        print(len(registros))

        self.assertEqual(len(registros) - inicio, 16, "Inserção incompleta")

if __name__ == '__main__':
    #run all test
    unittest.main() 
    

