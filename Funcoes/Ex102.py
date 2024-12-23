def leia_int():
    while True:
        entrada = input('Digite um número: ')
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Valor inválido. Por favor, digite um número inteiro.")

# usar função
numero = leia_int()
print(F'O numero digitado foi {numero}')


 