# Game: Pedra, Papel ou Tesoura
import random

opcoes = ['Pedra', 'Papel', 'Tesoura']
computador = random.choice(opcoes)

print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')

jogador = int(input('Qual é a sua jogada? '))
print('''
JO
KEN
PO !!!
''')

# Mostrar jogadas
print('{:=^40}'.format(' RESULTADO '))
print(f'Computador jogou: {computador}')
print(f'Jogador jogou: {opcoes[jogador]}')
print('=' * 40)

# Lógica do jogo
if jogador < 0 or jogador > 2:
    print('Jogada inválida!')
else:
    if computador == opcoes[jogador]:
        print('Empate!')
    elif (computador == 'Pedra' and opcoes[jogador] == 'Tesoura') or \
         (computador == 'Papel' and opcoes[jogador] == 'Pedra') or \
         (computador == 'Tesoura' and opcoes[jogador] == 'Papel'):
        print('Computador venceu!')
    else:
        print('Jogador venceu!')
