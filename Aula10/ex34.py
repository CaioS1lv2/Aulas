s = float(input('Qual é o seu salario do funcionario? R$'))
if s <= 900:
    aumento = s + (s * 20 / 100)
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${aumento:.2f} agora')
else:
    aumento1 = s + ( s * 10 / 100)
    print(f'Quem ganhava R${s:.2f} passa a ganhar R${aumento1:.2f} agora')

