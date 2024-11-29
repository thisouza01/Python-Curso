# PA 3.0

primeiroTermo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0

cond = 's'

# mostra proximo termo da PA
while cond == 's':
    pa = primeiroTermo + (razao * contador)
    print(pa)
    contador += 1
    print('Quer mostrar o proximo termo? "s ou n": ')
    cond = input()
    print()
