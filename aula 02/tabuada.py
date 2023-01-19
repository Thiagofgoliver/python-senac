# importar as bibliotecas do systema operacional
from os import system, name
# os = Biblioteca
# if = compararar informações (if= for / else = se nao )
# == igualdade / > maior />=maior igual
#! = diferente /<menor / menor /<= menor igual
# ao final so if sempre colocar o :

if (name == 'nt'):
    system('cls')

# if sempre usa ==

else:
    system('clear')

# cls se for windows / clear funciona no linux
print('****tabuada ****')

multiplicador = int(input('escreva um numero : '))


#criar um loop - repetição de codigo 
# for =  comando usado para criar um loop
# i = variavel (pode ser qualquer nome)
# range = usado para indicado quantas vezes sera feito o loop 
for i in range (11):
    resultado = i * multiplicador
    #print(' {}*{}={} ' .format(multiplicador,i,resultado))
    print(f'{multiplicador} * {i:<2} = {resultado}')


