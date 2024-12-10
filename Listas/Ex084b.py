# inicia listas
matriz = []
linha = []

# numero de linhas e colunas
num_linhas = 3
num_colunas = 3

while len(matriz) != num_linhas:
    # recebe numero
    numero = int(input('Numero: '))

    # adicion numero na linha
    linha.append(numero)

    if len(linha) == num_colunas:
        # adiciona a linha a matriz
        matriz.append(linha)
        # esvazia a linha
        linha = []

print(matriz)        
