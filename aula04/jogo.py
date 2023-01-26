"""
jogo:pedra,papel,tesoura
objetivo :
criar um jogo interativo iremos usar array (tupla)
bibliotecas:
random,os
funções :
iniciar jogo()

"""
from os import system ,name
import random
sair='S'
while (sair.upper()=='S'):

    system ('cls') if (name =='nt') else system ('clear')
    print(''' 
jogo:pedra,papel,tesoura
------------------------------------
escolha uma das opções para começar o jogar
[0]pedra
[1]papel
[2]tesoura
    ''')

    opcao = input('digite sua opção : ')
    continuar = True
    while(continuar):
        if(opcao.isdecimal()):
            opcao=int(opcao)
            if (opcao>=0 and opcao<=2):
                continuar= False
            else:
                opcao = input ('errou seu burro !digite um numero 0,1,2.se quiser sair aperte x : ')
                if(opcao.upper()=='X'):
                    print('sair')
                    exit()#comando para finalizar o codigo 


        else:
            opcao= input ('errou seu burro !digite um numero 0,1,2.se quiser sair aperte x : ')
            if(opcao.upper()=='X'):
                print('sair')
                exit()#comando para finalizar o codigo 
    opcao = int (opcao)
    computador = random.randint(0,2)

    jogadas = (("Empate","Computador Ganhou","Voce Ganhou"),
                ("voce ganhou","empate","computador ganhou"),
                ("computador ganhou","voce ganhou","empate"))
    pecas=('pedra','papel','tesoura')
    print(f'{pecas[computador]} x {pecas[opcao]}')            
    print(jogadas[computador][opcao])
    f_branco ="\033[47m"
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    letra_azul ="\033[1;34m"
    l_vermelha="\033[1;31m"
    f_amarelo = '\033[0;0m'
    padrao="\033[;7m"
    BOLD    = "\033[;1m"
    
    print (f_amarelo+letra_azul+
         (f'{pecas[computador]} x {pecas[opcao]}').center(79))
    print(f_branco+l_vermelha+
        (f'{jogadas[computador][opcao]})').center(79))
    print(padrao)


    sair=input('''

deseja jogar novamente?
aperte s (sim)
ou qualquer tecla para sair!
    ''')
   
   
