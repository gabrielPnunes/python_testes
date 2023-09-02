# from time import sleep
# for time in range(10, -1, -1):
#     sleep(0.3)
#     print(time)
# print('BUM!, BANG!, POOOO!')

# for par in range(2, 51, 2):
#     print(par, end=' ')
# print('acabou')

soma = 0
count = 0
for qui in range(1, 501, 2):
    if qui % 3 == 0:
        count = count + 1
        soma = soma + qui
print('A soma dos {} valores enviados é {} '.format(count, soma))
    
    
# n = int(input('Digite um número para formar uma tabuada: '))
# for tabuada in range(1, 11):
#     n * 1
#     n * 2
#     print(tabuada)