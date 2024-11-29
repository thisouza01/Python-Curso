# PA 2.0

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
numeroTermos = int(input('Digite a quantidade de termos: '))

contador = 0

while contador < numeroTermos:
    pa = primeiroTermo + (razao * contador)
    print(pa)
    contador += 1

