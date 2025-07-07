# # Escrever um programa para aprovar um emprestimo bancário.
# casa = float(int(input('valor da casa? R$')))
# salario = float(input('salario do comprador: R$ '))
# anos = int(input('Quantos anos vai pagar:'))
# prestação = casa / (anos * 12) 
# minimo = salario * 30 / 100

# print(f'Para pagar uma casa de R${casa:.2f} em {anos} a prestação será de R${prestação:.2f}')
# if prestação <= minimo:
#     print('Emprestimo Negado')
# else:
#     print('Emprestimo Aprovado')

nota = float(input('Digite uma nota:'))

if nota <= 0 and nota > 10:
    print(f'Nota inválida')
elif nota <=5:
    print(f'Reprovado')
elif nota == 5 or nota <=6.9:
    print(f'Recuperação')
elif nota == 7 or nota <= 9.9:
    print(f'Aprovado')
elif nota == 10:
    print(f'Parabens, nota máxima!')
print(f'Ai sim caio!')