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

# velo = int(input('A velocidade do carro era? '))
# if velo > 80:
#     print('Voce foi multado em R${}'.format(velo))
# else:
#     print('Voce está na velocidade permitida')

# n = int(input('Digite um número para ver se é par ou impar: '))
# if n / 2 :
#     print('Ele é par')
# else:
#     print('Impar')

# dist = float(input('A distância da viagem em KMs é: '))
# if dist <= 200:
#     print('O valor da viagem será de R${}'.format(dist * 0.50))
# else:
#     print('O valor da viagem será de R${}'.format(dist * 0.45))

# ano = int(input('Digite os dias do ano: '))
# if ano <= 365:
#     print('Esse ano não é bissexto')
# else:
#     print('Esse ano é bissexto')

# sal = float(input('Digite seu salário: '))
# if sal >= 1250:
#     print('O aumento do salário foi de R${}'.format(sal * 0.1))
# else:
#     print('O aumento do salário foi de R${}'.format(sal * 0.15))