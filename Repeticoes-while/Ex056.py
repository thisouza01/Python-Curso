from random import randint

# numero aleatório entre 1 e 10
numAleatorio = randint(1, 10)

# primeira chance de acertar
num = int(input('Número: '))

# inicia contador
cont = 1

# se numero for diferente, adciona 1 ao contador e pede para digitar outro numero novamente
if num == numAleatorio:
    print('Acertou!, precisou de {} tentativas'.format(cont))
else:    
    while num != numAleatorio:
        cont += 1
        print('Você errou. Digite outro número: ')
        num = int(input('Número: '))
    print('Acertou!, precisou de {} tentativas'.format(cont))
