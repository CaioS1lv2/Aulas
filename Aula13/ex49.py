n = int(input('Digite um nero para começar a sua tabuada:'))
for c in range(1, 10):
    n * c
print('{} x {:2} = {}'.format (n, 1, n*1))
print('{} x {:2} = {}'.format (n, 2, n*2))
print('{} x {:2} = {}'.format (n, 3, n*3))
print('{} x {:2} = {}'.format (n, 4, n*4))
print('{} x {:2} = {}'.format (n, 5, n*5))
print('{} x {:2} = {}'.format (n, 6, n*6))
print('{} x {:2} = {}'.format (n, 7, n*7))
print('{} x {:2} = {}'.format (n, 8, n*8))
print('{} x {:2} = {}'.format (n, 9, n*9))
print('{} x {:2} = {}'.format (n, 10, n*10))

# Correção 
n = int(input('Digite um nero para começar a sua tabuada:'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format (n, c, n*c))









# s = 0
# for c in range(1):
#     n = int(input('Digite um valor: '))
#     s += n
# print(f'o somatorio de todos os valores foi {s}')