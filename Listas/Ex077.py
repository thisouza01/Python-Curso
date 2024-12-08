lista_valores = [] 

while True:
    # Recebe o valor
    try:
        valor = int(input('Valor: '))
    except ValueError:
        print('Insira um número válido.')
        continue

    # Adiciona o valor se não estiver na lista
    if valor not in lista_valores:
        lista_valores.append(valor)
        print('Valor adicionado!')
    else:
        print('Valor já está na lista!')

    # Pergunta se o usuário quer continuar
    continuar = input('Quer continuar? (s/n): ').strip().lower()
    while continuar not in ('s', 'n'):
        print('Digite uma opção válida: s ou n')
        continuar = input('Quer continuar? (s/n): ').strip().lower()

    # Condição de saída
    if continuar == 'n':
        print('Lista final:', lista_valores)
        break
