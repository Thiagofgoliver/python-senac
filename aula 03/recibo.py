from os import system,name
from num2words import num2words

def validarNumero(numero):
    numero=numero.replace(',',',')
    try:
        resultado = float (numero)
    except:
        resultado = 0
    return resultado


system ('cls')if (name=='nt') else system ('clear')
print ('recibo'.center (8,"*"))
name = str (input ('informe o nome :'))
valor = str(input ('informe o valor :'))
validarNumero(valor)
extenso= (num2words(valor,to='currency',lang='pt_BR'))
valor =float (valor)
numeroBR =f'{valor:.2f}'.replace('.','.')
recibo =f'Recebemos de {name}\n o valor de {extenso} \n(R${numeroBR}).'
print (recibo)

#'''print(valor.isdecimal())

#if(valor.isdecimal ()):
    #print ('ok')'''
