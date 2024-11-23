# jogo de adivinhação
from random import randint

# gera numero inteiro aleatorio entre 0 e 5
numero = randint(0, 5)

# recebe input usuario
valor = int(input('Digite um numero entre  0 e 5: '))

# verifica se esta entre 0 e 5
if (valor >= 0) and (valor <= 5):

    # verifica se acertou o numero
    if valor == numero:
        print('Você acertou o numero que o computador escolheu, parabens!')
    else:
        print('Não foi dessa vez, o computador escolheu {}'.format(numero))

