# Maior e menor Valores
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
# Verficando quem é menor:
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<b and c<a:
    menor = c
print(f'O menor numero foi {menor}')
#verificando quem é o maior:
if a>b and a>c:
    maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior  = c
print(f'O maior numero foi {maior}')
