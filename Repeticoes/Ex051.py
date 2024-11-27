# Palíndromo

frase = str(input('Digite uma frase: '))

# remove espaços em branco
rmvEspaco = frase.strip()

# reverte a string
reverseStr = rmvEspaco[::-1]

# verifica se são iguais
if reverseStr == rmvEspaco:
    print('{} é palindromo'.format(frase))
else:
    print('Não é palindromo')    