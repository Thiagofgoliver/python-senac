from os import system
from requests import get # ler um endereço na internet
from bs4 import BeautifulSoup # interpretar uma página web

system('cls')

url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
response = get(url) #faz a leitura da pagina indicada
print(response) #imprimi a resposta da página
pagina = BeautifulSoup(response.text, 'html.parser') #interpreta o HTML
tabela = pagina.find_all('table')
arquivo = open("tabela_paises.html", mode="w", encoding="utf-8")
#arquivo.write(tabela[0].text)
print('Quantidade de tabelas:', len(tabela)) #contar alguma informação
linhas = tabela[0].find_all('tr') #separar as linhas da tabela[0] que é a dos paises 
print('Quantidade de linhas na tabela:' ,len(linhas))
for i in range(1, len(linhas)):
    colunas = linhas[i].find_all('td')
    link = colunas[1].find_all('a')
    url = f"https://pt.wikipedia.org{link[0].get('href')}"
    pais = get(url)
    resultado = BeautifulSoup(pais.text, 'html.parser')
    #print(link[0].get('href'))
    arquivo.write(str (i) + ' _ ' + (colunas[1].text).strip() + ' _ ' + (link[0].get('href')). strip() +'\n')

