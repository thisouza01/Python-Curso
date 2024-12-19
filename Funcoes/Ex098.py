from random import randint


# define funçoes

def sorteio():
    # inicia listas
    numeros = []

    for i in range(5):
        numeros.append(randint(1, 100))

    return numeros

def somaPar(numeros):
    # inicia soma
    soma = 0
    
    for i in numeros:
        if i % 2 == 0:
            soma += i

    return soma

# a lista recebe uma copia da lista 
lista_numeros = sorteio()[:]


print(lista_numeros)
print(f'A soma dos números pares criados pela função anterior é {somaPar(lista_numeros)}')            