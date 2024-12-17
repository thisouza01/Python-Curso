# inicia lista
lista_pessoas = []

# inicia soma_idade e contador
soma_idade = media = 0

while True:
    # recebe dado da pessoa    
    pessoa = {
        'nome': str(input('Nome: ')),
        'sexo': str(input('M / F: ')).strip().lower(),
        'idade': int(input('Idade: '))
    }

    # soma idade das pessoas cadastradas
    soma_idade += pessoa['idade']

    # envia para lista de pessoas
    lista_pessoas.append(pessoa.copy())

    # continuar?
    continuar = str(input('Continuar? (s / n)')).strip().lower()
    while continuar not in ('s', 'n'):
        print('Digite um valor válido')
        continuar = str(input('Continuar? (s / n)')).strip().lower()

    # saída
    if continuar == 'n':
        print(f'\nA quantidade pessoas cadastradas é {len(lista_pessoas)}')        
        break

# media das idades
media = soma_idade / len(lista_pessoas)
print(f'\nA media da soma das idades é {media:.2f}')

# verifica se é mulher
for pss in lista_pessoas:
    if pss['sexo'] in 'Ff':
        print(f'{pss["nome"]}', end='')
print()        

# lista com pessoas de idade acima da media
for pss in lista_pessoas:
    if pss['idade'] >= media:
        print(f'Pessoas com idade superior a media é: {pessoa["nome"]}')