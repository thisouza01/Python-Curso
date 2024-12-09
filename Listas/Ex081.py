while True:
    # recebe expressão
    expressao = str(input('Expressao para verificar: '))

    # verifica se tem parenteses
    qnt_inicio = expressao.count('(')
    qnt_final = expressao.count(')')

    # confirma se é valida
    if (qnt_final - qnt_inicio) != 0:
        print('Expressão inválida!')
    else:
        print('Expressão válida!')    

    # continuar
    continuar = str(input('Continuar? (s / n) '))

    while continuar.strip().lower() not in ('s', 'n'):
        print('Digite uma opção válida')
        continuar = str(input('Continuar? (s / n) '))
        
    if continuar.strip().lower() == 'n':
        break
