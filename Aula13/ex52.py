p = int(input('Digite um numero: '))
tot = 0
for c in range(1, p + 1):
   if p % c == 0:
       print(f'\033[33m{c}\033[m', end=' ')
       tot += 1
   else:   
       print(f'\033[31m{c}\033[m', end=' ')
   print(f'{c}', end=' ')
print(f'\nO numero {p} foi divisivel {tot} vezes')
if tot == 2:
    print(f'O numero \033[32m{p}\033[m e primo')
else:
    print(f'O numero {p} nao e primo')