# recebe dado do jogador
jogador = {
    'nome': str(input('Nome: ')),
    'partidas': int(input('Quantas partidas feitas: ')) 
}

# inicia lista de gols
gols  = []

# quantidade de gols
for partida in range(jogador['partidas']):
    gols.append(int(input(f'Quantos gols na partida {partida}: ')))


# atualiza dicionario de jogador
jogador.update({
    'quantidade de gols': sum(gols)
})

print(jogador)