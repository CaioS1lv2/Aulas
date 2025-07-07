ano = int(input('digite sua idade: '))
tk = str(input('Voce tem ingresso? '))
# if ano >= 18 and tk.lower() == 'S':
#     print('Entrada permitida! Bom filme!')
# elif ano > 18 or tk.lower() == 'N':
#     print('Entrada nao permitida')
# elif ano <= 17 and tk.lower() == 'S':
#     print('Entrada nao permitida')
#     ano = int(input('Digite sua idade: '))
# tk = input('Você tem ingresso? (sim/não): ')

if ano >= 18 and tk.lower() == 'sim':
    print('Entrada permitida! Bom filme!')
else:
    print('Entrada não permitida.')