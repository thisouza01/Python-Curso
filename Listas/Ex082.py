# lista geral
galera = []

# lista de cada pessoa
pessoa = []

# quatidade de pessoas
qnt_pessoas = 0

while True:
    # recebe dados
    nome = str(input('Nome: '))
    peso = float(input('Peso: '))

    # aumenta quantidade de pessoas
    qnt_pessoas += 1

    # adiciona na lista de pessoa
    pessoa.append(nome)
    pessoa.append(peso)

    # passo para lista das pessoas apenas os dados
    galera.append(pessoa[:])

    # limpo dados
    pessoa.clear()

    # continuar?
    continuar = str(input('Continuar? (s / n) '))
    while continuar not in ('s', 'n'):
        print('Use uma opção válida')
        continuar = str(input('Continuar? (s / n) '))

    # condição de saída
    if continuar.strip().lower() == 'n':
        
        mais_pesadas = []
        menos_pesadas = []

        # filtra as mais pesadas
        for pessoa in galera:
            if pessoa[1] >= 80:
                mais_pesadas.append(pessoa[0])
            else:
                menos_pesadas.append(pessoa[0])    

        # lista de pessoas
        print(galera)
        print()

        print('pessoas acima do peso:')
        for nome in mais_pesadas:
            print(f' - {nome}')

        print('pessoas abaixo do peso:')
        for nome in menos_pesadas:
            print(f' - {nome}')    

        break 