# radar eletronico

velocidade = int(input('Digite a velocidade que estava dirigindo: '))

if velocidade > 80:
    # calcula multa
    multa = (velocidade - 80) * 7

    print('Você foi multado! sua multa pela volicade foi de {} reais.'.format(multa))
else:
    print('Esta dirigindo dentro das leis!')    