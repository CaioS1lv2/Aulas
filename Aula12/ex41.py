#Classificando atletas
from datetime import date
ano = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - ano
print(f'O atleta tem {idade} ANOS')
if idade <= 10:
    print('Classificação: Mirim')
elif 11 <= idade <=15:
    print('Classsificação: Juvena')
elif idade == 17:
    print('Classificação: Sub17')
else:
    print('Classificação: ATLETA PROFISSIONAL')
   



  
