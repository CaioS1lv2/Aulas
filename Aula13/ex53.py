# Detector de palíndromos
# O programa irá verificar se a frase digitada é um palíndromo
# Um palíndromo é uma palavra ou frase que pode ser lida da mesma forma de trás para frente
frase = str(input('Digite uma frase: ')).strip().upper()
palavraas = frase.split()
junto = ''.join(palavraas)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print('Temos um palindromo!')
else:
    print('A frase digitada nao e um palindromo!')

