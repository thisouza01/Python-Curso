def leia_int():
    while True:
        try:
            inteiro = int(input('Inteiro: '))
        except (ValueError, TypeError):
            print('Erro: Digite um numero inteiro válido!!')
            continue
        else:
            return inteiro

def leia_float():
    while True:
        try:
            real = float(input('Real: '))
        except (ValueError, TypeError):
            print('Erro: Digite um numero inteiro válido!!')
            continue
        else:
            return real
        

print(leia_int())
print('-'*10)
print(leia_float())