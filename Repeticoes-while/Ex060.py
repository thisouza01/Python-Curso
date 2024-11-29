# PA 3.0

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0

cond = 's'

while cond == 's':
    pa = primeiroTermo + (razao * contador)
    print(pa)
    contador += 1
    print('Quer continuar? "s ou n": ')
    cond = input()
    print()
