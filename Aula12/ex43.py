peso = int(input('Qual é o seu peso? (Kg)'))
alt = float(input('Qual é sua altura? (m)'))
imc = peso / (alt * alt)
if imc >= 40:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Vc está em obsesidade mórbida, cuidado!')
elif 35 <= imc <= 39.90:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Vc está com obesidade nivel 2, se cuide!')
elif 30 <= imc <= 34.90:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Vc está obeso!')
elif 25 <= imc <= 29.90:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Vc está acima do peso')
else:
    print(f'O IMC dessa pessoa é de {imc:.2f}')
    print('Parabéns, continue assim!')
