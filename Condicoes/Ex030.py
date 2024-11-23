# Ano bissexto

ano = int(input('Digite um ano: '))

anoBissexto = ano % 4

if anoBissexto == 0:
    print('O ano {} é um ano bissexto'.format(ano))
else:
    print('O ano {} não é um ano bissexto'.format(ano))    