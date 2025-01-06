import moeda
# crie um modulo chamado moeda.py -> aumentar(), diminuir(), dobro(), metade()
# usar no programa principal
valor = float(input('Valor: '))

# metade
print(f'A metade de {valor} é {moeda.metade(valor)}')

# dobro
print(f'O dobro de {valor} é {moeda.dobro(valor)}')

# aumento de 10%
print(f'Um aumento de 10% no valor de {valor} é {moeda.aumento(valor)}')

# redução de 13%
print(f'Uma diminuição de 13% no valor de {valor} é {moeda.reducao(valor)}')

# pacote utilidades que tenha dois modulos internos chamados moeda e dado
# transfira todas as funçoes utilizadas para os pacotes e mantenha funcionando

#modulo dado -> leiaDinheiro() -> validação de dados