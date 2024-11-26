# Aprovando emprestimo

valorCasa = float(input('Digite o valor da casa: '))
salComprador = float(input('Digite seu salário: '))
qntAnos = int(input('Quantos anos para pagar a casa: '))

# calcula parcela
parcelaMensal = valorCasa / (12 * qntAnos)

# aprova emprestimo
if parcelaMensal < salComprador * 0.30:
    print('Empréstimo aprovado no valor de {}'.format(parcelaMensal))
else:
    print('Empréstimo negado!')    