from random import randint

# incia lista
jogadas = []

# inicia contador para marcar o ID do jogador
contador = 1

# recebe 4 vezes o inteiro e salva em um dicionario
for _ in range(4):
    jogada = {
        "jogador": int(contador),
        "dado": randint(1, 6)
    }

    contador += 1

    # envia a jogada para a lista de jogadas
    jogadas.append(jogada)

# ranking dos jogadores
for valor in jogadas:
    print(valor)    
