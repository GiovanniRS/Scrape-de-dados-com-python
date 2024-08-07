# Importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
# Importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep

# Abrindo o navegador para começar a automacação, utilizando o webdriver
chrome = webdriver.Chrome()