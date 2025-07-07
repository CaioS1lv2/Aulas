p = int(input('Digite um numero: '))
for c in range(1, p + 1):
    if p % c == 0:
        print('O número é primo')
    else:
        print('O número não é primo')