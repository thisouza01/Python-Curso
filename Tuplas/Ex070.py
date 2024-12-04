# tupla
tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# condição de parada
parar = 'n'

# ler numero
while True:
    numero = int(input('Numero: '))

    if numero < 0 or numero > 20:
        print('Numero fora da sequencia')
        
    if parar == 's':
        break    

# mostrar numero por extenso
print(tupla[numero])
