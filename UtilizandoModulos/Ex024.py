#ler uma frase e mostra quantidade de letra 'a', qual a primeira vez que aparece e a posição da ultima vez em que aparece

frase = str(input('Digite uma frase: '))

quantidadeA = frase.count('a')
primeiroA = frase.find('a')
ultimoA = frase.rfind('a')

print('A quantidade de caracteres " a " nessa frase é {} '.format(quantidadeA))
print('O primeiro " a " aparece na posição {}'.format(primeiroA))
print('O ultimo " a " aparece na posição {}'.format(ultimoA))