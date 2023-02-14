from os import system 

def calculator(): # def criar função 

    system ('cls') #apagar terminal do windows 
    #while = faça enquanto a condição for verdadeira 
    #while true = loop infinito 
    
    while True: #while loop 
       

       # print = escreva na tela 
        
        print("Selecione a operação desejada:")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair da Calculadora")

        
        #choice variavel para guardar escolha do menu 
        # corrigir esse comando 
       
        choice =  input("Informe sua escolha (1/2/3/4/5): ") 
        #if para sair do while, usando break ira parar o loop  

    

        if choice == "5":
            break #
        elif choice == "1" or choice == "2" or choice == "3" or choice == "4" :

            num1 = int(input("Informe o primeiro número: "))
            num2 = int(input("Informe o segundo número: "))
            # if / elif / else
            

            if choice == "1":
                
                print(f'o resultado da soma sera: {num1} + {num2} = {num1 + num2}')
            elif choice == "2":
                print(f'o resultado da subtração sera: {num1} - {num2} = {num1 - num2}')
            elif choice == "3":
                print(f'o resultado da Multiplicação sera: {num1}* {num2} = {num1 * num2}')
            
            elif choice == "4":
                
                print(f'o resultado da divisão sera: {num1}/ {num2} = {num1 / num2}')
           
        else:
            print("Escolha inválida, tente novamente")
        input('APERTE ENTER PARA CONTINUAR ')
        system ('cls')
# termino da função 

# chama a função 

calculator()

