# Ordem de precedencia
# 1 > ()
# 2 > **
# 3 > * / % //
# 4 > + -

# ler um numero inteiro e mostrar seu sucessor e seu antecessor
num = int(input('Digite um numero inteiro: '))
sucessor = num + 1
antecessor = num - 1
print('Seu antecessor é {} e seu sucessor é {} '.format(antecessor, sucessor))
