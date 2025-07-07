#Radar eletrônico
km = float(int(input('velocidade: ')))
if km >= 80:
    print('Vc foi multado! excedeu o limite de velocidade de 80Km/h!')
    multa = (km-80) * 7
    print('vc deve pagar uma multa de R${:.2f}!'.format(multa))
else:
    print('Continue dirigindo com segurança!')