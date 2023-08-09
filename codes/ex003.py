from math import floor
number = float(input('Digite um número: '))
print(floor(number))

import math
cat_op = float(input('Qual o tamanho do cateto oposto? '))
cat_adj = float(input('Qual o tamnhgo do cateto adjacente? '))
hipo = (cat_adj * cat_adj + cat_op * cat_op)
print('O valor da hipotenusa é {}'.format(math.sqrt(hipo))) 
