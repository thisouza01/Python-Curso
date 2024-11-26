soma = 0

for i in range(1, 7):
    numero = int(input('Digite um numero: '))
    # verifica se é par
    if numero % 2 == 0:
        soma += numero

print('A soma total é {}'.format(soma))        