soma = 0
count = 0
for qui in range(1, 501, 2):
    if qui % 3 == 0:
        count = count + 1
        soma = soma + qui
print('A soma dos {} valores enviados é {} '.format(count, soma))

