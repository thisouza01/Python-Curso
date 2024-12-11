from random import randint

# inicia lista
jogos = []

# quantidade de jogos para serem feitos
qnt_jogos = int(input('Quantidade de jogos para serem feitos: '))

# criar a sequencia de 6 numeros entre 1 e 60
for i in range(qnt_jogos):
    # reinicia a lista
    numeros = []

    while len(numeros) < 6:
        numero = randint(1, 60)
        # verifica se tem numero ja na lista
        if numero not in numeros:
            numeros.append(numero)   
  
    # adiciona lista de numeros a lista de jogos
    jogos.append(numeros[:])

print(jogos)
            