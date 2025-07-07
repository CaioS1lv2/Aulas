pro = float(input('Qual o preço do produto? R$'))
novo = pro - (pro * 5 / 100)

print(' o preço do produto que custava R${}, na promoçao de 5% vai custar R${}'.format(pro, novo))