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

class CodigoTestado1():
    def limparPreco(preco):
        if preco == None or preco == '':
            return -1
        try:
            preco = preco.replace('R$ ','')
            preco = preco.replace(',','.')
            preco = float(preco)
        except:
            preco = -1
        return preco

    # FUNCÕES PAGUE MENOS
    def coletar_preco_paguemenos(medicamento, driver):
        driver.get(medicamento['link'])
        try:
            preco = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[4]/div/div/div/section/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div[1]/div[1]/div/div[2]/div/div[2]/span/span'))
            )
            preco = preco.text
        except:
            try:
                preco = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div/div[1]/div/div/div/div[4]/div/div/div/section/div/div/div/div[1]/div[2]/div/div[3]/div/div[5]/div/div/div[1]/div/div[2]/div/div/span/span'))
                )
                preco = preco.text
            except:
                preco = '-1'
        medicamento['preco'] = CodigoTestado1.limparPreco(preco)

    def coletar_paguemenos(driver):
        medicamentos_paguemenos = [
         #   {
          #      'idfarmacia': 1,
          #      'idmedicamento': 1,
                ## FUI INTIMADO!!!
           #     'preco': -1
           # }, #dipirona
            {
                'idfarmacia': 1,
                'idmedicamento': 2,
                'link': 'https://www.paguemenos.com.br/advil-400mg-leve-8-pague-6-capsulas/p',
                'preco': -1
            }, #advil
            {
                'idfarmacia': 1,
                'idmedicamento': 3,
                'link': 'https://www.paguemenos.com.br/engov-com-12-comprimidos/p',
                'preco': -1
            }, #engov
            {
                'idfarmacia': 1,
                'idmedicamento': 4,
                'link': 'https://www.paguemenos.com.br/neosaldina-com-10-drageas/p',
                'preco': -1
            }, #neosaldina
            {
                'idfarmacia': 1,
                'idmedicamento': 5,
                'link': 'https://www.paguemenos.com.br/dorflex-36-comprimidos/p',
                'preco': -1
            }, #dorflex
            {
                'idfarmacia': 1,
                'idmedicamento': 6,
                'link': 'https://www.paguemenos.com.br/novalgina-1g-10-comprimidos/p',
                'preco': -1
            }, #novalgina
            {
                'idfarmacia': 1,
                'idmedicamento': 7,
                'link': 'https://www.paguemenos.com.br/sal-de-fruta-eno-efervescente-2-saches-de-5g/p',
                'preco': -1
            }, #eno
            {
                'idfarmacia': 1,
                'idmedicamento': 8,
                'link': 'https://www.paguemenos.com.br/neosoro-solucao-nasal-adulto-com-30-ml/p',
                'preco': -1
            }, #neosoro
            {
                'idfarmacia': 1,
                'idmedicamento': 9,
                'link': 'https://www.paguemenos.com.br/merthiolate-spray-30ml/p',
                'preco': -1
            }, #mertthiolate
            {
                'idfarmacia': 1,
                'idmedicamento': 10,
                'link': 'https://www.paguemenos.com.br/estomazil-em-po-sem-sabor-5g-com-6-envelope/p',
                'preco': -1
            }, #estomazil
            {
                'idfarmacia': 1,
                'idmedicamento': 11,
                'link': 'https://www.paguemenos.com.br/allegra-60mg-com-10-comprimidos/p',
                'preco': -1
            }, #allegra
            {
                'idfarmacia': 1,
                'idmedicamento': 12,
                'link': 'https://www.paguemenos.com.br/descongestionante-vick-vaporub-30g/p',
                'preco': -1
            }, #vic vaborrub
            {
                'idfarmacia': 1,
                'idmedicamento': 13,
                'link': 'https://www.paguemenos.com.br/polaramine-2mg-caixa-com-20-comprimidos/p',
                'preco': -1
            }, #polaramine
            {
                'idfarmacia': 1,
                'idmedicamento': 14,
                'link': 'https://www.paguemenos.com.br/dramin-b6-com-30-comprimidos/p',
                'preco': -1
            }, #dramin
            {
                'idfarmacia': 1,
                'idmedicamento': 15,
                'link': 'https://www.paguemenos.com.br/espironolactona-25mg-com-30-comprimidos-generico-geolab/p',
                'preco': -1
            }, #espironolactona
            {
                'idfarmacia': 1,
                'idmedicamento': 16,
                'link': 'https://www.paguemenos.com.br/insulina-novolin-r-10ml/p',
                'preco': -1
            } #insulina
        ]
        for medicamento in medicamentos_paguemenos:
            CodigoTestado1.coletar_preco_paguemenos(medicamento, driver)	
        return medicamentos_paguemenos
