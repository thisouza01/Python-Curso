# Progressão aritimética

primeiroTermo = float(input('Digite o primeiro termo: '))

razao = float(input('Digite a razâo: '))

numTermos = 10

pa = [primeiroTermo + (i * razao) for i in range(numTermos)]

print("Os primeiros", numTermos, "termos da PA são:", pa)