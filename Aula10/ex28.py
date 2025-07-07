# Jogo da Adivinhação v.1.0
import random 
num1 = random.randint(0, 5)
us = int(input('Qual o numero certo? '))
if us == num1:
    print('vc acertou parabens!')
else:
    print('Vc errou!')
print('Bom jogo! o numero certo é {} '.format(num1))
# sEGUNDA FORMA DE SE FAZER!
import random 
num1 = random.randint(0, 5)
us = int(input('Qual o numero certo? '))
print('VC acertou' if us == num1 else 'Vc errou!')
print('Bom jogo! o numero certo é {} '.format(num1))