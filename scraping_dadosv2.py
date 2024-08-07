# Importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep

# Abrindo o navegador para começar a automacação, utilizando o webdriver
chrome = webdriver.Chrome()

chrome.get('https://books.toscrape.com/')
sleep(1)

livros = chrome.find_elements(By.XPATH, '//article[@class="product_pod"]')

for livro in livros:
    titulo = livro.find_element(By.XPATH, './h3/a')
    print(titulo.get_attribute('title'))

sleep(10)