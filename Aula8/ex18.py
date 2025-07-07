# seno, Cosseno e Tangente

import math 
an = float('Digite o  angulo que voce deseja : ')
seno = math.sin(math.radians(an))
print('o angulo de  {} tem o SENO de {}'.format(an, seno))
cosseno = math.cos(math.radian(an))
print('O  angulo de {} tem o cosseno de {:.2f}'.format(an, cosseno))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem a TANGENTE de {:.2f}'.format(an, tangente))