# Par oou Impar
from random import randint

resulta = 0

contVitoria = 0

while True: # loop infinito
    
    # sua escolha
    numero = int(input('Numero: '))
    escolha = int(input('Par ou Impar? [1 \ 2]: '))

   # verificação de saída
    if numero < 1 or (escolha != 1 and escolha != 2):
        break

    # escolha do computador    
    numeroComp = randint(1, 10)

    # somar 
    soma = numero + numeroComp

    # verifica quem ganhou
    resultado = numero + numeroComp

    if escolha == 1:
        if resultado % 2 == 0:
            print(f'Você ganhou! Deu par, a soma deu {soma}')
            contVitoria += 1
        elif resultado % 2 != 0:
            print('Você perdeu! Deu Impar!')
            print(f'Voce ganhou {contVitoria} vezes seguidas!')
            break

    elif escolha == 2:
        if resultado % 2 == 0:
            print('Você perdeu! Deu par')
            print(f'Voce ganhou {contVitoria} vezes seguidas!')
            break
        elif resultado % 2 != 0:
            print(f'Você ganhou! Deu Impar, a soma deu {soma}') 
            contVitoria += 1


