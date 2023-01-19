
#criar uma tabuada completa
from os import system, name 
# if ternario (if feito em apenas uma linha )

system ('cls') if(name=='nt') else system ('clear')
print ('-*****Tabuada*****-')
linha = ''
linha2 =''
for i in range (11):

    for multiplicador in range(1, 6):
        resultado = multiplicador *i  
        linha += f'{multiplicador}*{i:<2} = {resultado:<3} | '
        resultado2 = (multiplicador + 5)*i
        linha2 += f'{multiplicador+5}*{i:<2} = {resultado2:<3} | '
    linha +='\n'
    linha2 +='\n'
print(linha)
print('')
print (linha2)
  


