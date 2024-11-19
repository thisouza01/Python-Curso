# ler um numero inteiro e mostre sua tabuada
num = int(input('Digite um número inteiro: '))
contador = 0

for contador in range(10):
    print('{} x {} = {}'.format(num, contador + 1, num * (contador + 1)))
    


