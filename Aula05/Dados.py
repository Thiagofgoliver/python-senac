class importacao :
    def impCategoria(self):
        import os 
        # getcwd pega  o  caminho da minha pasta atual 
        #print (os.getcwd())



        # caminho de onde está o arquivo

        Arquivo =os.path.dirname(os.path.realpath(__file__)) + '\\BaseDados\\categorias.csv'
        # abrir o arquivo 

        #"r " = read (leitura )/'w' = write (escrever)
        # 'RW' ou 'wr = leitura e escrita
        # encoding - tipo de arquivo (acentos e  caracteres especias)


        categorias = open (Arquivo,'r',encoding='utf-8')
        #criar uma variavel para guardar valores

        listaCategoria = {} #dicionario muito parecido json


        contador = 0 
        listaCategoria["Tabela"] = "categoria"
        listaCategoria ["Dados"] =""
        dadoscategoria ={}
        for linhas in categorias :

            colunas = linhas.strip().split(';')
            contador +=1
            dadoscategoria [colunas [0]] = {'nome':colunas[1],'descrição':colunas[2]}
            #print (dadoscategoria)
            

            #print(colunas)


        listaCategoria["Total"]=contador
        listaCategoria ["Dados"] = dadoscategoria
        return listaCategoria
        #print(contador)
