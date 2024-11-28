# recebe valores
num1 = float(input('Digite um valor: '))
num2 = float(input('Digite outro valor: '))

# mostra opções
print()
print('1 - SOMAR \n2 - MULTIPLICAR \n3 - MAIOR \n4- NOVOS NUMEROS \n5- SAIR')
print()

# escolhas
escolha = int(input('Escolha uma opção: '))

# verificação
while escolha != 5:
    if escolha ==1:
        #soma numeros
        soma = num1 + num2
        print(soma)
        escolha = int(input('Escolha uma opção: '))
    elif escolha == 2:
        # multiplica numeros    
        multiplica = num1 * num2
        print(multiplica)
        escolha = int(input('Escolha uma opção: '))
    elif escolha == 3:
        # maior numero
        maior = max(num1, num2)    
        print(maior)
        escolha = int(input('Escolha uma opção: '))
    elif escolha == 4:
        print('Digite outro numero para adicionar')
        novoNum = float(input())
        print(novoNum)
        escolha = int(input('Escolha uma opção: '))
    else:
        print('Digite um valor possível!')     

