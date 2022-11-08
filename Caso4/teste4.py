import unittest
from codigoTestado4 import *

engine = create_engine('mysql+mysqlconnector://root:root@localhost/farmaticos')

class TesteRaspagem(unittest.TestCase):
   def teste(self):
        real = CodigoTestado4.extracao()
        self.assertEqual(real, 16, "Extração incompleta")

if __name__ == '__main__':
    #run all test
    unittest.main() 
    

