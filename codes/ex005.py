from random import randint
from time import sleep
compu = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em número de 0 a 5...Tente adivinhar')
print('-=-' * 20)
pla = int(input('Em que número pensei? '))
print('PROCESSANDO...')
sleep(2)
if compu == pla:
    print('Você acertou o meu número')
else:
    print('Você errou, eu pensei no número {} e não no número {}'.format(compu, pla))

velo = float(input('Qual a velocidade atual do carro? '))
if velo > 80:
    print('Você exedeu o limite de velocidade permitido')
    multa = (velo - 80) * 7
    print('Você foi multado em R${:.2f}'.format(multa))
print('Dirija com segurança')

n = int(input('Digite um número para ver se é par ou impar: '))
res = n % 2
if res == 0:
    print('O seu número é par')
else:
    print('O seu número é impar')

dist = float(input('A distância da viagem em KMs é: '))
if dist <= 200:
    pre = dist * 0.50
else:
    pre = dist * 0.45
print('O preço da viagem será de R${:.2f}'.format(pre))

from datetime import date
ano = int(input('Digite o ano, se quiser o ano atual coloque zero: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} não é bissexto'.format(ano))

num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
num3 = int(input('Digite o terceiro número: '))
menor = num2
if num1<num2 and num1<num3:
    menor = num1
if num3<num2 and num3<num1:
    menor = num3
maior = num2
if num1>num2 and num1>num3:
    maior = num1
if num3>num2 and num3>num1:
    maior = num3
print('O menor número foi {} e o maior {}'.format(menor, maior))

sal = float(input('Digite seu salário:R$ '))
if sal <= 1250:
    sal_n = sal + (sal * 15 / 100)
else:
    sal_n = sal + (sal * 10 / 100)
print('O seu salario de R${} aumentou para R${}'.format(sal, sal_n))

print('-=-' * 20)
print('analisador de triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento de reta: '))
r2 = float(input('Segundo segmento de reta: '))
r3 = float(input('Terceiro segmento de reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos formam um triangulo')
else: 
    print('Os segmentos acima não formam triangulos5')