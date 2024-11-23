# maior e menor valores

listaNumeros = []

for i in range(3):
    listaNumeros.append(int(input('Digite um numero: ')))

# maior numero da lista
maiorNumero = max(listaNumeros)
# menor numero da lista
menorNumero = min(listaNumeros)      

print('O maior numero da lista é {} e o menor numero da lista é {}'.format(maiorNumero, menorNumero))