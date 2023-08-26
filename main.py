casa = float(input('Qual o valor da casa?:R$ '))
sal = float(input('Qual o seu salário?:RS '))
anos = int(input('Quantos anos irá financiar?: '))
parc = casa / (anos * 12)
minimo = sal * 0.3
print('Para a casa de R${:.2f} em {} anos, a prestação será de R${:.2f}'.format(casa, anos, parc))
if parc >= minimo:
    print('Você não foi aprovado')
else:
    print('Você foi aprovado')


number = int(input('Digite um número inteiro: '))
print('''[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL ''')
opc = int(input('A sua opção: '))
if opc == 1:
    print('O número {} convertido para BINÁRIO fica {}'.format(number, bin(number)[2:]))
elif opc == 2:
    print('O número {} convertido para OCTAL fica {}'.format(number, oct(number)[2:]))
elif opc == 3:
    print('O número {} convertido para HEXADECIMAL fica {}'.format(number, hex(number)[2:]))
else:
    print('Opção invalida')


n1 = int(input('Digite o primeiro número inteiro: '))
n2 = int(input('Digite o segundo número inteiro: '))
if n1 > n2:
    print('O PRIMEIRO número, {} é maior que o segundo {}'.format(n1, n2))
elif n1 < n2:
    print('O SEGUNDO número {}, é maior que o primeiro número {}'.format(n2, n1))
else:
    print('Os valores {} e {} são IGUAIS'.format(n1, n2))


from datetime import date
nasc = int(input('Ano de nascimento: '))
atual = date.today().year
idade_1 = atual - nasc
print('Quem nasceu em {} tem {} anos em {}'.format(nasc, idade_1, atual))
if idade_1 == 18:
    print('Você tem que se alistar IMEDIATAMENTE')
elif idade_1 < 18:
    saldo = 18 - idade_1 
    ano_alis = atual + saldo
    print('Ainda faltam {} ano(s) para o seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano_alis))
elif idade_1 > 18:
    saldo = idade_1 - 18
    ano_alis = atual - saldo
    print('Você deveria ter se alista há {} ano(s)'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano_alis))


not1 = float(input('Digite a sua primeira nota: '))
not2 = float(input('Digite a sua segunda nota: '))
media = (not1 + not2) / 2
if media < 5:
    print('A sua média foi de {}, por tanto está REPROVADO'.format(media))
elif 7 > media >= 5:
    print('A sua média foi de {}, por tanto está em recuperação'.format(media))
else:
    print('Parabéns você foi aprovado com media {}'.format(media))


from datetime import date
nasc_1 = int(input('Ano de nascimento: '))
actu =  date.today().year
idade = actu - nasc_1
print('O atleta tem {} anos'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:
    print('Classificação: MASTER')

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo', end='')
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2!= r3 != r1 :
        print(' ESCALENO')
    else:
        print(' ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

peso = float(input('Digite o seu peso atual(KG): '))
altura = float(input('Digite sua altura(M): '))
imc = peso / (altura ** 2)
print(imc)
if imc < 18.5:
    print('Está abaixo do peso, o seu imc é {:.1f}'.format(imc))
elif 18.5 <= imc < 25:
    print('Está no peso ideal, o seu imc é {:.1f}'.format(imc))
elif 25 <= imc < 30:
    print('Está com sobrepeso, o seu imc é {:.1f}'.format(imc))
elif 30 <= imc < 40:
    print('Está com obsidade, o seu imc é de {:.1f}'.format(imc))
else:
    print('Está com obsidade mórbida, o seu imc é de {:.1f}'.format(imc))

# preco_prod = float(input('Digite o preço do produto :R$ '))
# avista_d = preco_prod - (preco_prod * 0.1)
# if avista_d:
#     print('O preço do produto a vista em dinheiro ou cartão, fica em R${}, ja com os 10% de desconto'.format(avista_d))