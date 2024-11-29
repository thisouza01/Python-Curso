numInteiro = int(input('Numero inteiro: '))

primeiroNum = 0
segundoNum = 1

lista = []

while numInteiro >= 1:
    resposta = primeiroNum + segundoNum

    lista.append(resposta)

    primeiroNum = segundoNum
    segundoNum = resposta

    numInteiro -= 1

print(lista)    