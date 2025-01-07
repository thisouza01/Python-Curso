import moeda as moeda
# usar no programa principal

def leia_dinheiro(msg):
    # inicia se é valido o input
    valido = False

    # enquanto valido for False
    while not valido:
        # recebe valor
        valor = str(input(msg))
        # verifica
        if valor.isalpha() or valor == ' ':
            print('Valor inválido!!')
        else:
            # sai do loop
            valido = True
            return float(valor)


# recebe valor
valor = leia_dinheiro('Digite um valor: R$')

# resumo -> valor, aumento e redução
moeda.resumo(valor, 20, 40)

# metade
print(f'A metade de {moeda.moeda(valor)} é {moeda.metade(valor, True)}')

# dobro
print(f'O dobro de {moeda.moeda(valor)} é {moeda.dobro(valor, True)}')