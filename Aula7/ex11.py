pare1 = float(input('Largura da parede:'))
pare2 = float(input('Altura da parede:'))

dimen = pare1 * pare2
print('Sua parede tem a dimensao de {}x{} e sua área é de {}m²'.format(pare1, pare2, dimen))
tinta = dimen / 2
print('Para pintar essa area vc ira precisar de {}l de tinta'.format(tinta))