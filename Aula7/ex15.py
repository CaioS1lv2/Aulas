# Km total a pagar 
dias = int(input(' Quantos dias alugados? '))
km = float(input('Qauntos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R4{:.2f}'.format(pago))

