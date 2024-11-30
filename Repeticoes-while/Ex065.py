# Tabuada 3.0

while True:  # Loop infinito
    contador = 0
    numero = int(input('Digite um número inteiro (negativo para parar): '))

    if numero < 0:  # Condição de saída
        print('Adeus!')
        break

    # Exibe a tabuada do número
    while contador <= 10:
        print(f'{numero} x {contador} = {numero * contador}')
        contador += 1
    
    print()  