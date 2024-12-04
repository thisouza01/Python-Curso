lista = []
lista_par = []

num = 3

for i in range(4):
    lista.append(int(input('Numero: ')))

# converte para tupla
tupla = tuple(lista)
print()

# mostra tupla
print(tupla)
print()

# quantos 9
print(f'Apareceram {tupla.count(9)} numeros 9 na tupla')
print()

# posição do primeiro 3
if num in tupla:
    posicao = tupla.index(num)
    print(f'O primeiro 3 aparece na posição {posicao}')
else:
    print('Não tem na tupla')     
print()

# numeros pares
for numero in tupla:
    if numero % 2 == 0:
        lista_par.append(numero)

tupla_par = tuple(lista_par)        
print(f'Os numero pares digitados são: {tupla_par}')

