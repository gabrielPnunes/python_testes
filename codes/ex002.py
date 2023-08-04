n1 = int(input('Digite um número: '))
ant = n1 - 1
suce = n1 + 1
print('o antecessor de {}, é o número {}, e o sucessor desse número é o {}.'.format(n1, ant, suce))
#ou
print('O antecessor de {}, é o número {}, e o sucessor desse número é o {}'.format(n1, (n1 - 1),(n1 + 1)))

n = int(input('Digite um número: '))
db = n * 2
tp = n * 3
rq = n ** (1/2)
print('O dobro de {} vale {},\ne o triplo é {}. \ne a raiz quadrada é {:.2f}'.format(n, db, tp, rq))

not1 = float(input('Digite a primeira nota: '))
not2 = float(input('Digite a segunda nota: '))
med = (not1 + not2) / 2
print('A primeira nota é {}.'.format(not1))
print('A segunda nota é {}.'.format(not2))
print('A média entre {:.1f} e {:.1f} é igual a {:.1f}.'.format(not1, not2, med))

metro = float(input('Quantos metros? '))
km = metro / 1000
hm = metro / 100
dam = metro /10
dm = metro * 10
cm = metro * 100
mm = metro * 1000
print('{} metros equivale a:'.format(metro))
print('{:.4f}KMs'.format(km))
print('{:.3f}HMs'.format(hm))
print('{:.2f}DAMs'.format(dam))
print('{:.0f}DMs'.format(dm))
print('{:.0f}CMs'.format(cm))
print('{:.0f}MMs'.format(mm))


number = int(input('Digite um número para ver a tabuada: '))
print( '-' * 12)
print('{} X {:2} = {}'.format(number, 1, number * 1))
print('{} X {:2} = {}'.format(number, 2, number * 2))
print('{} X {:2} = {}'.format(number, 3, number * 3))
print('{} X {:2} = {}'.format(number, 4, number * 4))
print('{} X {:2} = {}'.format(number, 5, number * 5))
print('{} X {:2} = {}'.format(number, 6, number * 6))
print('{} X {:2} = {}'.format(number, 7, number * 7))
print('{} X {:2} = {}'.format(number, 8, number * 8))
print('{} X {:2} = {}'.format(number, 9, number * 9))
print('{} X {:2} = {}'.format(number, 10, number * 10))
print( '-' * 12)



brl = float(input('Digite a quantia em reais: R$ '))
usd = brl / 4.92
print('Convertando a quantia de R${:.2f} em dolares, levando em condsideração a cotação atual dará {:.2f}US$.'.format(brl, usd))

alt = float(input("Digite a altura: "))
larg = float(input("Digite a largura: "))
area = alt * larg
quant_t = area / 2
print('Para pintar a area de {}m², é preciso {}L de tinta'.format(area, quant_t))

prod = float(input('O preço do produto é? '))
desct = prod - (prod * 0.05)
print('O preço do produto é R${}, mas com desconto de 5% fica R${:.2f}'.format(prod, desct))

sal = float(input('Qual o seu atual salário?R$ '))
desco = sal + (sal * 0.15)
print('O salário inicial era de R${:.2f}, mas com o aumento de 15% ficou R${:.2f}.'.format(sal, desco))

temp_at = float(input('Digite a temperatura atual em °C : '))
temp_f = temp_at * 1.8 + 32
print('A temperatura de {}°C é equivalente a {}°F'.format(temp_at, temp_f))

d = int(input('Digite por quantos dias deseja alugar o carro: '))
km = float(input('Quantos KMs foram percorridos? '))
t  = (d * 60) + (km * 0.15)
print('O total a se pagar é R${:.2f}'.format(t))
