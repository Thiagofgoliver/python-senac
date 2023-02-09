from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from getpass import getpass

def clicar (xpath):
    try:
        clicar = chrome.find_element (By.XPATH , xpath)
        clicar.click ()
        sleep(3)
    except:
        print(f'Erro no XPATH:{xpath}')

def Escrever (xpath, texto):
    try:
        digitar = chrome.find_element (By.XPATH, xpath)
        digitar.send_keys (texto)
        sleep (3)
    except :
        print (f'ERRO XPATH:{xpath}')
email = input (" escreva seu email: ")
passoard = getpass ("escreva sua senha: ")
        

site = 'https://www.sp.senac.br' # time / sleep usados para  gerar uma espera no codigo 
# o time sera usado para que de tempo da pagina carregar antes de execultar algo 
chrome = webdriver.Chrome ()
chrome.get(site)

# botao para ignorar cockies
botãoEntendi = '//*[@id="mm-0"]/div[4]/div'  # botão cockie
clicar (botãoEntendi)
sleep (5)

#botão das 3 barrinhas 
botãoBurguer = '//*[@id="menu-mobile-ssp"]'
clicar (botãoBurguer)

botãoLogin = '//*[@id="txtLoginNaoLogadoMob"]'
clicar(botãoLogin) # botao login 

#escrever email
login = '//*[@id="login-email"]'
clicar (login)
Escrever(login ,email)


#escrever senha 
senha = '//*[@id="login-password"]'
Escrever(senha,passoard)
clicar (senha)

#botao para entrar 
botaoEntrar = '//*[@id="btnLoginHeader"]'
clicar (botaoEntrar)

sleep (50)