# Alistamento Militar! Dificil 
from datetime import date #modulo
atual = date.today().year
ano = int(input('Ano de nascimento: '))
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}')
if ano == 18:
    print(f'Ja esta na hora de se alistar IMEDIATAMENTE!')
elif ano < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} anos para o alistamento')
elif ano > 18:
    saldo = idade - 18
    print(f' voce ja devia ter se alistado há {saldo} anos')