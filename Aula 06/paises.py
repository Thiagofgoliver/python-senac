'''
    Web Scraping - instalar bibliotecas
    > pip install requests
    > pip install beautifulsoup4
'''
from os import system, path
from requests import get  # ler um endereço na internet
from bs4 import BeautifulSoup # interpretar uma página web
system('cls')
url = 'https://pt.wikipedia.org/wiki/Lista_de_pa%C3%ADses_por_popula%C3%A7%C3%A3o'
resposta = get(url) #faz a leitura da pagina indicada
print(resposta) #imprimi a resposta da página 
pagina = BeautifulSoup(resposta.text, 'html.parser') #interpreta o HTML
tabela = pagina.find_all('table')
pasta = path.dirname(path.realpath(__file__))
arquivo = open(f"{pasta}\\tabela_paises.txt", mode="w", encoding="utf-8")
#arquivo.write(tabela[0].text)
print('Quantidade de tabelas:', len(tabela)) # contar alguma informação
linhas = tabela[0].find_all('tr') #separar as linhas da tabela[0] que é a dos paises
print('Quantidade de linhas na tabela:' ,len(linhas))
for i in range(1, 10):
    colunas = linhas[i].find_all('td')
    link = colunas[1].find_all('a')
    url = f"https://pt.wikipedia.org{link[0].get('href')}"
    pais = get(url)
    resultado = BeautifulSoup(pais.text, 'lxml')
    tabelaPais = resultado.find_all('table')
    #print(len(tabelaPais))
    

    #print(tabelaPais[0])
    colunasPais =tabelaPais [0].find_all('td')
    #print(len(colunasPais))
    validar = 0 
    for i in range (0, len (colunasPais)):
        #print (colunasPais[i].text )
        if (validar == 1):
                capital = (colunasPais[i].text).strip()
                validar = 0
                print (capital)
        if (colunasPais[i].text).strip()=="Capital":
                validar = 1

       
    #print(link[0].get('href'))
    arquivo.write(str(i) + ' - ' + (colunas[1].text).strip() + 
        ' - ' + (link[0].get('href')). strip() + '\n'
        '_'+capital)
        
