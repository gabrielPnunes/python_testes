nome = str(input('Qual o seu nome?: '))
if nome == 'Bella':
    print('Que nome lindo!!')
elif nome == 'Joao' or nome == 'Paulo' or nome == 'Maria' or nome == 'Joana':
    print('Seu nome é muito comum')
elif nome in 'Ana Maria Jose Jesus':
    print('Que nome diferente')
else:   
    print('Você tem um nome comum')
print('Tenha um bom dia, {}!'.format(nome))