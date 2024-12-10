# inicia listas
matriz = []
linha = []

# inicia soma
soma = 0
soma_par = 0

# numero de linhas e colunas
num_linhas = 3
num_colunas = 3

while len(matriz) != num_linhas:
    numero = int(input('Numero: '))

    # verifica se numero é par
    if numero % 2 == 0:
        soma_par += numero

    # adiciona numero a linha
    linha.append(numero)

    if len(linha) == num_colunas:
        # adiciona a linha a matriz
        matriz.append(linha)
        # zera linha
        linha = []

# soma valores da terceira coluna
soma = matriz[0][2] + matriz[1][2] + matriz[2][2]  

# maior valor segunda coluna
maior_valor = max(matriz[0][1], matriz[1][1], matriz[2][1])

print(f'A matriz é: {matriz}') 
print(f'A soma de numeros pares é: {soma_par}') 
print(f'A soma dos numeros da terceira coluna é: {soma}') 
print(f'O maior valor da segunda coluna é: {maior_valor}') 
