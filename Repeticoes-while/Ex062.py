contador = 0
soma = 0

# enquanto verdadeiro
while True:
    numero = int(input('Numero: '))
    if numero != 999:
        contador += 1
        soma += numero
        print('Digite outro numero ou 999 para parar')
    elif numero == 999:
        print('Adeus!')
        print('A soma dos numeros deu {}'.format(soma))
        break