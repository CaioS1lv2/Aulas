# Soma dos pares
soma = 0
cont = 0 
for c in range(1, 7):
    num = int(input(f'digite o {c} valor: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Voce informou {cont} números Pares  e a soma foi {soma}')