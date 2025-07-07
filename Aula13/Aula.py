for c in range(0,10):
    print('Oi')
print('Fim')
# ---------------------------- # -------------------------------------
# irá escrever de 0 a 9
for c in range(0,10):
    print(c)
print('Fim')
#-----------------------------------------------------------------------
# contar de trás para frente tem que ter o passo negativo -
# irá escrever de 6 a 1
# de onde começa até onde e vai (6, 0, -1)
for c in range(6, 0, -1):
    print(c)
print('Fim')
#----------------------------------------
# de onde começa até onde e vai e pulando (0, 7, 2)
for c in range(0, 7, 2):
    print(c)
print('Fim')
#---------------------------------------------------
#Exemplo com Input o número que o usuário digitar
# irá escrever de 0 até o número digitado
# o +1 é para incluir o número digitado
# se não colocar o +1 ele não inclui o número digitado
# por exemplo se digitar 5, ele vai de 0 a 4
n = int(input('Digite um numero:' ))
for c in range(0, n+1):
    print(c)
print('FIM')
#----------------------------------------------------------------
#Exemplo com Inicio, Fim e Passo
i = int(input('Inicio'))
f = int(input('Fim:'))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('Fim')
#----------------------------------------------
# somatorio de valores o s é o somatorio de todos os valores
# o usuário digitará 4 valores e o programa irá somar todos eles
# o s começa com 0 e vai somando os valores digitados
# o for irá repetir 4 vezes, ou seja, o usuário irá digitar 4 valores
# e o programa irá somar todos eles
s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'o somatorio de todos os valores foi {s}')