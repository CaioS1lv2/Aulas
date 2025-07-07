# Desenvolva um programa que pergunte a distancia da viagem em Km e calacule o preço da passagem 
dis = float(input('Qual a distancia da sua viagem? '))
if dis <= 200:
    preco = dis *0.50
    print(f'vc ira pagar R${preco:.2f} pelos {dis}Km')
else:
    preço = dis * 0.45
    print(f'como a viagemn passou de 200km vc irá pagar R${preço:.2f}, pq a viagem a cima disso tera o custo de R$0.45')