numInteiro = int(input('Numero inteiro: '))

# começa
primeiroNum = 0
segundoNum = 1

# coloca os numeros em uma lista
lista = []

while numInteiro >= 1:
    resposta = primeiroNum + segundoNum

    lista.append(resposta)

# troca o segundo numero pelo primeiro
    primeiroNum = segundoNum

# troca a soma pelo segundo numero    
    segundoNum = resposta

# diminui o contador 
    numInteiro -= 1

print(lista)    