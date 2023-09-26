for a in range(1,11):
    print(a)
print('fim')

for b in range (5, 0, -1):
    print(b)
print('fim')

for c in range(0, 10, 3):
    print(c)
print('fim')

d = int(input('Digite um número: '))
for d in range(0, d + 1):
    print(d)

e = int(input('Início: '))
f = int(input('Fim: '))
g = int(input('Passo: '))
for h in range (e, f + 1, g):
    print(h)

h = 0
for i in range(0,2):
    j = int(input('Digite um número: '))
    h += j
print('O somatório de todos os valores foi {}'.format(h))

frutas = ["maçã", "banana", "cereja"]
for x in frutas(0, 2):
print(x)