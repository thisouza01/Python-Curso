# Custo da viagem

distanciaViagem = int(input('Qual a distancia da sua viagem? '))

if distanciaViagem <= 200:
    precoPassagem = distanciaViagem * 0.50
    print('Sua viagem custará {} reais'.format(precoPassagem))
else:
    precoPassagem = distanciaViagem * 0.45
    print('Sua viagem custará {} reais'.format(precoPassagem))    