nome = input("qual o seu nome")
print("É um prazer te conhecer,{}!".format(nome))

dia = input("qual o dia do seu nascimento?")
mes = input("qual o mês em que nasceu?")
ano = input("ano em que nasceu?")
print("Você nasceu no dia", dia, "do" , mes , "de", ano) 

n1 = int(input("digite um numero")) 
n2 = int(input("digite mais um numero"))
s = n1 + n2
print("soma entre {0} e {1} vale {2}".format(n1, n2, s))

n = input("Insira algo: ")
print("O tipo primitivo desse valor é?", type(n))
print("Só tem espaços?", n.isspace())
print("É um número?", n.isnumeric())
print("E alfabético?", n.isalpha())
print("É um alfanúmerico?", n.isalnum())
print("Está em maiúsculas?", n.isupper())
print("Está em minúsculas?", n.islower())
print("Está capitalizada", n.istitle())