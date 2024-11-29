numero = int(input('Digite um numero para fatorar: '))

fatorial = 1

contador = numero

# fatorial = fatorial * numero
while contador >= 1:
    fatorial *= contador
    contador -= 1
    
print(fatorial)
    
    