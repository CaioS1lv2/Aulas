""" Faça um progrtama que leia um numero de 0 a 9999 e mostre na 
tela cada um dos digitos separados """

num = int(input('informe um numero: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}'.format(num))
print('unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('milhar: {}'.format(m))   