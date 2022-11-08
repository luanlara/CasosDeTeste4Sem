from ast import Try
from dataclasses import replace
from os import rename
import sys
import time
from unicodedata import decimal
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

## O grupo ainda não entrgou o código 

class CodigoTestado4():
    def extracao():
        
        engine = create_engine('mysql+mysqlconnector://root:root@localhost/farmaticos')

        registros = 0

        with Session(engine) as sessao, sessao.begin():
            registros = sessao.execute(text("SELECT count(*) FROM medicamento")).scalar()
            print(registros)
        
        sessao.close()

        return registros