#Par ou Ímpar?
numero = int(input('Me diga um numero qualquer: '))
resultado = numero % 2
if resultado == 0:
    print('O numero {}  é Par'.format(numero))
else:
    print('O numero {} é Impar'.format(numero))