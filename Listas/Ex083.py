# abre lista
lista_valores = []
lista_par = []
lista_impar = []

# verifica e envia para cada lista
for numero in range(7):
    if numero % 2 == 0:
        lista_par.append(numero)
    else:
        lista_impar.append(numero)

# junta as listas
lista_valores.append(lista_par[:])
lista_valores.append(lista_impar[:])

# mostra a lista completa e separada
print(lista_valores)