dolar = float(input('Qaunto dinheiro voce tem na carteira? R$:'))

real = dolar / 5.82
print('Com dolares${:.2f} vc pode comprar reais${:.2f}'.format(real, dolar))