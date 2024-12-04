from random import randint

lista = []

for i in range(5):
    numInteiro = randint(1, 10)
    lista.append(numInteiro)

tupla = tuple(lista)
# lista gerada
print(tupla)

print()
# maior numero
maiorNum = max(tupla)
print(f'Maior numero : {maiorNum}')

print()
# menor numero
menorNum = min(tupla)
print(f'Maior numero : {menorNum}')