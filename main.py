from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd

empresas = ['btg','safra','itau','bradesco','santander','microsoft','facebook','inter','amazon','daniel','petrobras']


navegador = webdriver.Chrome()
infos = {"Empresa": [], "Valor" : []}
for empresa in empresas:
    navegador.get("https://www.google.com/search?q=acoes+{}".format(empresa))
    try:
        navegador.find_element(by=By.CLASS_NAME, value='aviV4d')
        page_content = navegador.page_source
        site = BeautifulSoup(page_content, 'html.parser')
        rastreios = site.findAll('span', attrs={'jsname': "vWLAgc"})
        x = rastreios[0]
        infos['Empresa'].append(empresa)
        infos['Valor'].append(x.getText())
    except:
        pass
print(pd.DataFrame(infos))
navegador.quit()
