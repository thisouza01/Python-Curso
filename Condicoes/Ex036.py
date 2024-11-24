# ler dois numeros inteiros e comparar
# O primeiro é maior ou ou segundo é maior ou sao iguais

num1 = int(input('Digite um numero inteiro: '))
num2 = int(input('Digite outro numero inteiro: '))

if num1 == num2:
    print('Ambos números são iguais')
elif num1 > num2:
    print('O primeiro número é maior que o segundo')
else:
    print('O segundo número é maior que o primeiro')        