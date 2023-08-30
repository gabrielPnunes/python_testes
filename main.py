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