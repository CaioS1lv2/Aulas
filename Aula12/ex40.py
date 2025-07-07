# Média so que com condições 
nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))
resu = (nota1 + nota2) / 2
print(f'Tirando {nota1} e {nota2}, a média do aluno é {resu}')
if resu >= 7.0:
    print('O aluno esta APROVADO')
elif resu < 7.0:
    print('o aluno esta REPROVADO!')
