# Importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep

# Abrindo o navegador para começar a automacação, utilizando o webdriver
chrome = webdriver.Chrome()
# Abrindo uma url
chrome.get('https://books.toscrape.com/')
sleep(1)

#Buscando o elemento do titulo do livro utilizando o xpath
titulo = chrome.find_element(By.XPATH, '/html/body/div/div/div/div/section/div[2]/ol/li[1]/article/h3/a')
#Clicando no titulo do livro
titulo.click()
sleep(1)

#Buscando o elemento do titulo do livro dentro da pagina do livro utilizando o xpath
titulo_especifico = chrome.find_element(By.XPATH, '/html/body/div/div/div[2]/div[2]/article/div[1]/div[2]/h1')
#Imprimindo conteudo que esta entre as tags do html
print(titulo_especifico.text)

#Voltando a pagina do chrome para a anterior
chrome.back()

sleep(10)