# define a função
def ficha(nome, gol = 0):
   print(f'\nO jogador {nome} fez {gol} gols!')

# recebe nome e quantidade de gols
nome_jogador = str(input('Nome do jogador: '))
if len(nome_jogador) == 0:
   nome_jogador = 'desconhecido'

qnt_gols = str(input('Quantidade de gols: '))
if qnt_gols.isnumeric():
   qnt_gols = int(qnt_gols)
else:
   qnt_gols = 0   


ficha(nome_jogador, qnt_gols)

