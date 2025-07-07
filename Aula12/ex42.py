# analisando triangulos
r1 = float(input('Primeiro segmento:'))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento:'))
if r1 == r2 and r3:
    print('O segmento é Equilátero')
elif (r1 < r2 and r2 == r3) or (r3 < r2 and r2 == r1) or (r2 < r3 and r3 == r1):
    print('O segmento tem dois lados iguais, entao é Isósceles')
else:
    print('Todos os lados sao diferentes entao é um Escaleno')