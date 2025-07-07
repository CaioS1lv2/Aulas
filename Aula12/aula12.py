#Condições Aninhadas \n uso das condições If, elif e else

nome = str(input('Qual é o seu nome? '))
if nome == 'Caio':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Isadora':
    print('Seu nome é bem popular no Brasil!') 
elif nome in 'Pablo, Gustavo, Wesley, carlos':
    print('Belo nome Masculino')
print(f'Tenha um bom dia {nome}')
