import moeda
# usar no programa principal
valor = float(input('Valor: '))

# metade
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')

# dobro
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')

# aumento de 10%
print(f'Um aumento de 10% no valor de {moeda.moeda(valor)} é {moeda.moeda(moeda.aumento(valor))}')

# redução de 13%
print(f'Uma diminuição de 13% no valor de {moeda.moeda(valor)} é {moeda.moeda(moeda.reducao(valor))}')

