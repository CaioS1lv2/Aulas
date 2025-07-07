# Primeira e última ocorrência de uma string
nome = str(input("Digite uma frase: ")).upper().strip()
print('A letra A aparece {} vezes na frase'.format(nome.count('A')))
print('A primeira letra A apareceu na posiçao {}'.format(nome.find('A')+1))
print("a ultima letra A apareceu na posiçao {}".format(nome.rfind('A')+1))