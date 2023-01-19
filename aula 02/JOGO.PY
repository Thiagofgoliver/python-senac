import random
#random.randrage (numero inicial , numero final) feito para sortear um numero 
valor = random.randrange(1,100)
print('tente adivinhar o  numero de 1 a 100 ')
numero =0
while (valor!=numero):

    numero = int (input ('informe o numero :'))

    if (numero == valor):
        print ('voce acertou ')
    elif (numero > valor):
        print ('o numero era menor')
    elif (numero < valor):
        print ('o numero ERA  maior')
print (f'o numero era :{valor}')


