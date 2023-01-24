#bibliotecas python 
import math 

#help(math) 
# int = inteiro / float = numero com casas decimais

'''num1 = 10
num2 = 3
resultado = num1 / num2
print (resultado)
print (f'{resultado:2f}')'''

num1 = int (input ('informe um numero '))
num2 = int (input ('informe um numero '))
resultado = num1 / num2
print (resultado)
print (f'{resultado:2f}')
print (round(resultado,2))
#ceil= arredondamento para cima
print (math.ceil(resultado))
# pega a parte inteira do numero 
print (math.floor (resultado))
# mod = pega o resto de uma divisao
print (math.fmod(num1,num2))

