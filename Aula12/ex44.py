#Gerenciador de Pagamentos
print('{:=^40}'.format (' LOJAS CAIOs  '))
P = int(input('Preço das compras: R$'))
print( '''  FORMAS DE PAGAMENTO  
[ 1 ] a vista dinheiro/cheque
[ 2 ] a vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
n1 = int(input('Qual é a opção? '))
if n1 == 4:
    par = int(input('Quantas parcelas? '))
    resu = P / par + 80
    print(f'Sua comrpa será percelada em {par}x de {resu:.2f} com juros! ')
    # print(f'Sua compra de R${P:.2f} vai custar R${resu:.2f} no final')
elif n1 == 3:
    par = int(input('Quantas vezes ira parcelar ? '))
    resu = P / par
    print(f'Sua compra será parcelada em {par}x de R${resu:.2f} sem juros!')
elif n1 == 2:
    resu = P - ( P * 10 / 100)
    print(f'Sua compra de R${P} vai custar {resu:.2f} no final!')
else: 
    print(f'Total da compra R${P:.2f}')