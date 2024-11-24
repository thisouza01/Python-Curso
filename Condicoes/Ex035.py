# ler numero inteiro
# escolha 1 binário, 2 octal, 3 hexadecimal

numInteiro = int(input('Digite um numero inteiro: '))

print('1 - Binário \n2 - Octal \n3 - hexadecimal')
opcao = int(input('Escolha uma opção: '))

if opcao == 1:
    binario = bin(numInteiro)[2:]
    print('Numero {} em binário é {}'.format(numInteiro, binario))
elif opcao == 2:
    octal = oct(numInteiro)[2:]
    print('Numero {} em octal é {}'.format(numInteiro, octal))
elif opcao == 3:
    hexadecimal = hex(numInteiro)[2:]
    print('Numero {} em hexadecimal é {}'.format(numInteiro, hexadecimal))    
