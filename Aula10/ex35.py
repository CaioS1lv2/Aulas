#Analisador Triangulo v1.0 
print('-='*20)
print('Analisador de Triangulo')
print('-='*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r2 + r3 and r3 < r1 + r2:
    print(f'Os segmentos acima PODEM FORMAR UM SEGMENTO!')
else:
    print('Os segmentos acime NAO PODE FORMAR UM TRIANGULO!')
