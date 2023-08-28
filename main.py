

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