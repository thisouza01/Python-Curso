# inicia tabela de jogadores
jogadores = []

while True:
    # inicia tabela de gols
    gols = []

    # recebe dado dos jogadores
    jogador = {
        'nome': str(input('Nome: ')),
        'quantidade_partidas': int(input('Quantidade de partidas: '))
    }

    # recebe quantidade de gols
    for partida in range(jogador['quantidade_partidas']):
        gols.append(int(input(f'Quantidade de gols na partida {partida}: ')))

    # update em jogador
    jogador.update({
        'gols': gols,
        'soma_gols': sum(gols)
    })

    # envia jogar para lista de jogadores
    jogadores.append(jogador)

    # continuar?
    continuar = str(input('Continuar? (s / n) ')).strip().lower()
    while continuar not in ('s', 'n'):
        print('Digite um valor válido!')
        continuar = str(input('Continuar? (s / n) ')).strip().lower()

    # condição de saída
    if continuar == 'n':
        for jogador in jogadores:
            print(jogador)
        break

while True:
    analise = str(input('Quer ver análise de algum jogador? (s / n): ')).strip().lower()
    while analise not in ('s', 'n'):
        print('Digite um valor válido!')
        analise = str(input('Quer ver análise de algum jogador? (s / n): ')).strip().lower()

    if analise == 'n':
        print('Encerrando o programa.')
        break

    escolha = int(input('Qual índice do jogador? '))
    if 0 <= escolha < len(jogadores):
        jogador = jogadores[escolha]
        print(f"\nAnálise do jogador {jogador['nome']}:")
        print(f"  Partidas jogadas: {jogador['quantidade_partidas']}")
        print(f"  Gols por partida: {jogador['gols']}")
        print(f"  Total de gols: {jogador['soma_gols']}\n")
    else:
        print('Índice inválido! Tente novamente.')