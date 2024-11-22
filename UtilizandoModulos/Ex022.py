#ler o nome da cidade e mostra se comeca com a plavra SANTO

cidade = str(input('Digite uma cidade: '))

cidadeSanto = cidade.find('SANTO')

if cidadeSanto == 0:
    print(cidadeSanto)
else:
    print('Não tem a palavra SANTO na cidade digitada')