from random import randint 

# inicia lista
lista_valores = []

# gera quantidade de valores de valores aleatorios e gera valores alaorios para a lista
for i in range(randint(1, 10)):
    lista_valores.append(randint(1, 10))

# define função de achar o maior valor na lista
def maior_valor(lista):
    lista = lista_valores[:]
    print(f'O maior valor da lista é {max(lista)}')


print(lista_valores)
print()
maior_valor(lista_valores)