def notas(lista, situacao=False):
    soma_notas = 0

    # quantidade de notas
    qnt_notas = len(lista)

    # soma as notas 
    for nota in lista:
        soma_notas += nota

    # media
    media = soma_notas / qnt_notas    

    # maior nota
    maior_nota = max(lista)

    # menor nota
    menor_nota = min(lista)

    print(f'tem {qnt_notas} notas inseridas')
    print(f'A media das notas é {media:.2f}')
    print(f'A maior nota é {maior_nota}')
    print(f'A menor nota é {menor_nota}')

    if situacao == True:
        if media >= 7:
            print('Situação Boa')
        elif  media < 7 and media >= 4:
            print('Situação Preocupante')  
        else:
            print('Situação Péssima')      


notas([1, 6, 7.5, 4.8, 5.4], True)    