# inicia lista
lista_pessoas = []
lista_mulheres = []

# inicia soma_idade e contador
soma_idade = cont = 0

while True:
    # recebe dado da pessoa    
    pessoa = {
        'nome': str(input('Nome: ')),
        'sexo': str(input('M / F: ')).strip().lower(),
        'idade': int(input('Idade: '))
    }

    # envia para lista de pessoas
    lista_pessoas.append(pessoa)

    # continuar?
    continuar = str(input('Continuar? (s / n)')).strip().lower()
    while continuar not in ('s', 'n'):
        print('Digite um valor válido')
        continuar = str(input('Continuar? (s / n)')).strip().lower()

    # saída
    if continuar == 'n':
        # media de idades
        for _ in lista_pessoas:
            soma_idade += pessoa['idade']
            cont += 1
        media_idade = soma_idade / cont

        # verifica se é mulher
        for pss in lista_pessoas:
            if pessoa['sexo'] == 'f':
                lista_mulheres.append(pessoa)

        print(f'A lista de mulheres é {lista_mulheres}')
        print(f'A média das idades dessa lista é {media_idade}')        
        break