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

print('{:=^40}'.format(' LOJAS GUANABARA '))
preco = float(input('Qual o preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO 
[ 1 ] á vista dinheiro ou cheque
[ 2 ] á vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opcao = int(input('Qual a opção? '))
if opcao == 1:
    total = preco - (preco * 10/100)
elif opcao == 2:
    total = preco - (preco * 5/100)
elif opcao == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcela em 2x de {:.2f} SEM JUROS '.format(parcela))
elif opcao == 4:
    total = preco + (preco * 20/100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc 
    print('Sua compra será parcela em {}x de R${:.2f} COM JUROS'.format(totalparc, parcela))
else:
    total = preco
    print('Sua compra será INVÁLIDA de pagamento. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final '.format(preco, total))

from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opção são:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual a sua jogada? '))
print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura!!')
sleep(1)
print('-=' * 10)
print('O jogador jogou {}'.format(itens[jogador]))
print('O computador jogou {}'.format(itens[computador]))
print('-=' * 10)
if computador == 0:
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('O jogador venceu!!')
    elif jogador == 2:
        print('O computador venceu')
    else:
        print('Jogada inválida')
elif computador == 1: 
    if jogador == 0:
        print('O computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('O jogador venceu!!')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print('O jogador venceu!!')
    elif jogador == 1:
        print('O computador venceu')
    elif jogador == 2:
        print('Empate')
else:
    print('Jogada inválida')