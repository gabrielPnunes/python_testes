cval = float(input('Qual o valor da casa?: '))
sal = float(input('Qual o seu salário?: '))
qano = int(input('Quantos anos irá financiar?: '))
parc = cval / (qano * 12)
print(parc)
if parc > (sal * 0.3):
    print('Você não foi aprovado')
else:
    print('Você foi aprovado')

n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print('O primeiro número, {} é maior que o segundo {}'.format(n1, n2))
elif n1 < n2:
    print('O segundo número {}, é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os valores {} e {} são iguais'.format(n1, n2))

not1 = float(input('Digite a sua primeira nota: '))
not2 = float(input('Digite a sua segunda nota: '))
media = (not1 + not2) / 2
if media < 5:
    print('A sua média foi de {}, por tanto está reprovado'.format(media))
elif media <= 5 or media < 6.9:
    print('A sua média foi de {}, por tanto está em recuperação'.format(media))
else:
    print('Parabéns você foi aprovado com media {}'.format(media))

idade = int(input('Digite a sua idade: '))
if idade <= 9:
    print('Com a idade de {} anos, a sua categoria é a mirim'.format(idade))
elif idade <= 14:
    print('Com a idade de {} anos, a sua categoria é a infantil'.format(idade))
elif idade <= 19:   
    print('Com a idade de {} anos, a sua categoria é a junior'.format(idade))
elif idade == 20:
    print('Com a idade de {} anos, a sua categoria é a senior'.format(idade))
else:
    print('Com a idade de {} anos, a sua categoria é a master'.format(idade))

peso = float(input('Digite o seu peso atual: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print(imc)
if imc < 18.5:
    print('Está abaixo do peso, o seu imc é {:.2f}'.format(imc))
elif imc == 18.5 or imc <= 25:
    print('Está no peso ideal, o seu imc é {:.2f}'.format(imc))
elif imc == 25 or imc <= 30:
    print('Está com sobrepeso, o seu imc é {:.2f}'.format(imc))
elif imc == 30 or imc <= 40:
    print('Está com obsidade, o seu imc é de {:.2f}'.format(imc))
else:
    print('Está com obsidade mórbida, o seu imc é de {:.2f}'.format(imc))

# preco_prod = float(input('Digite o preço do produto :R$ '))
# avista_d = preco_prod - (preco_prod * 0.1)
# if avista_d:
#     print('O preço do produto a vista em dinheiro ou cartão, fica em R${}, ja com os 10% de desconto'.format(avista_d))
