# flag de parada

numeroInteiro = 0

soma = 0

while True:
    # Enquanto nao coloca 999 vai somando, se colocar ignora ele
    numeroInteiro = int(input('Numero inteiro: '))

    if numeroInteiro != 999:
        soma += numeroInteiro
    else:
        print(f'A soma dos numeros deu {soma}')
        break