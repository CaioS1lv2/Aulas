salario = float(input('Qual é o salario do funcionario? R$'))
aumento = salario + (salario * 15 / 100)
print('um funcinario que ganhava R${}, com 15% de aumento passa a receber R${:.2f}'.format(salario, aumento))