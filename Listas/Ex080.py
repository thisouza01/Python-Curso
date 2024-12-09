# inicia lista
lista_pares = []
lista_impares = []

while True:

    # recebe numero
    try:
        numero = int(input('Numero: '))
    except ValueError:
        print('Digite um numero inteiro')
        continue

    # verifica se é par ou impar
    if numero % 2 == 0:
        lista_pares.append(numero)
    elif numero % 2 != 0:
        lista_impares.append(numero)
    else:
        print('Digite um valor válido')

    # cotinuar?
    continuar = str(input('Quer continuar? (s / n) '))
    while continuar.lower().strip() not in ('s', 'n'):
        print('Digite corretamente uma opção')
        continuar = str(input('Quer continuar? (s / n) '))

    # condição saída    
    if continuar == 'n':
        print(f'Lista de numeros pares {lista_pares}')                
        print(f'Lista de numeros impares {lista_impares}')  
        break              
