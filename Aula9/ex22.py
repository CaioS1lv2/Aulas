nome = str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome....')
print('Seu nome e letras maiúsculas é {}'.format(nome.upper()))
print('Se nome em letras minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count('  ')))
# print('Seu primeiro nome é {} e ele tem {} letras'.format(nome[0:4], nome.count()))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
