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

# Organizar o ranking dos jogadores pelo valor do dado em ordem decrescente
ranking = sorted(jogadas, key=lambda x: x["dado"], reverse=True)

# Exibir o ranking dos jogadores
print("Ranking dos jogadores:")
for posicao, valor in enumerate(ranking, start=1):
    print(f"{posicao}º lugar: Jogador {valor['jogador']} com dado {valor['dado']}")   
