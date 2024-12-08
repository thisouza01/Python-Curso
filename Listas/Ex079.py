# inicia lista
lista_numeros = []

# inicia loop
while True:
    
    # testa numero
    try:
        numero = int(input('Numero: '))
    except ValueError:
        print('Digite um numero inteiro!')
        continue

    # envia pra lista
    lista_numeros.append(numero)

    # Pergunta se o usuário quer continuar
    continuar = str(input('Quer continuar? (s/n): '))
    while continuar not in ('s', 'n'):
        print('Digite uma opção válida')
        continuar = str(input('Quer continuar? (s/n): '))

    # condição de saída
    if continuar == 's':

        # quantidade de numeros dentro da lista
        qnt_numeros = len(lista_numeros)
        print(f'A quantidade de numeros dentro da lista é {qnt_numeros}')

        # ordem crescente
        ordenado = lista_numeros.sort(reverse=True)  
        print(f'A lista na ordem decrescente é {ordenado}')

        # verifica se o 5 foi adicionado
        if 5 in lista_numeros:
            print(f'O 5 esta no indece{lista_numeros.index(5)}')


        break    


