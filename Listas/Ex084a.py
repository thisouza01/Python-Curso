from random import randint

# gera nove numeros aleatorios entre 1 e 10
numeros = [randint(1,10) for _ in range(9)]

# cria matriz
matriz = []
for i in range(3):
    # a cada numero inserido na lista, diminui um
    linha = [[numeros.pop()] for _ in range(3)]
    # adiciona a linha a matriz 3 vezes
    matriz.append(linha)

print(f'{matriz[0]}\n'f'{matriz[1]}\n'f'{matriz[2]}')    