# jokenpo
from random import randint

# escolha do computador
numAleatorio = randint(1, 3)

if numAleatorio == 1:
    escolhaComp = 'Pedra'
elif numAleatorio == 2:
    escolhaComp = 'Papel'
elif numAleatorio == 3:
    escolhaComp = 'Tesoura'

# escolha do usuário
print('Escolha uma opção')
escolhaUser = str(input('Pedra \nPapel \nTesoura \n'))  
print()
          
# partida
if escolhaComp == escolhaUser:
    print('{} x {} : Empate!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Pedra' and escolhaUser == 'Papel':
    print('{} x {} : Usuário ganhou!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Pedra' and escolhaUser == 'Tesoura':
    print('{} x {} : Computador ganhou!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Papel' and escolhaUser == 'Pedra':
    print('{} x {} : Computador ganhou!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Papel' and escolhaUser == 'Tesoura':
    print('{} x {} : Usuário ganhou!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Tesoura' and escolhaUser == 'Pedra':        
    print('{} x {} : Usuário ganhou!'.format(escolhaComp, escolhaUser))
elif escolhaComp == 'Tesoura' and escolhaUser == 'Papel':
    print('{} x {} : Computador ganhou!'.format(escolhaComp, escolhaUser))
