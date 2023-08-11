from math import trunc
number = float(input('Digite um número quebrado: '))
print('O valor inteiro é {}'.format(trunc(number)))

from math import sqrt
cat_op = float(input('Qual o tamanho do cateto oposto? '))
cat_adj = float(input('Qual o tamnhgo do cateto adjacente? '))
hipo = (cat_adj ** 2 + cat_op ** 2)
print('O valor da hipotenusa é {:.2f}'.format(sqrt(hipo)))

from math import sin, cos, tan, radians
ang = float(input('Digite um ângulo: '))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print('O ângulo de {} tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {} tem o COSSENO de {:.2f}'.format(ang, coss))
print('O ângulo de {} tem a TANGENTE de {:.2f}'.format(ang, tang))

from random import choice
prim = str(input('Primeiro aluno: '))
second = str(input('Segundo aluno: '))
terc = str(input('Terceiro aluno: '))
quart = str(input('Quarto aluno: '))
lista = [prim, second, terc, quart]
esco = choice(lista)
print('O aluno escolhido foi {}'.format(esco))

from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('Terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lis = [n1, n2, n3, n4]
escol = shuffle(lis)
print('A ordem de apresentação será: {}'.format(lis))
