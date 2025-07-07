#Procurando uma string dentro de outra

nome = str(input('Qual é o seu nome completo? ')).strip()

print('Seu nome tem silva? {} '.format('silva' in  nome.lower()))