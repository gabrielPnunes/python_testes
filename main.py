#MÚLTIPLOS VALORES PARA UMA VARIÁVEIS
a, b, c = "limão", "laranja", "manga"
print(a)
print(b)
print(c)

#UM VALOR PARA MÚLTIPLAS VARIÁVEIS
d = e = f = "banana"
print(d)
print(e)
print(f)

#DESCOMPACTAR UMA LISTA
vegetais = ["batata", "alface", "cenoura"]
g, h, i = vegetais
print(g)
print(h)
print(i)

#VARIAVEL LOCAL
x = "otimo"

def MinhaFuncao():
    print("Pyton é " + x)

MinhaFuncao()

#VARIAVEL GLOBAL
x2 = "Maneirão"

def MinhaFuncao2():
    global x2
    x2 = "maneralho"
MinhaFuncao2()

print("Python é " + x2)
