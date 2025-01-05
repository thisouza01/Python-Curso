# adapte o exercicio anterior. crie uma função moeda()

# recebe valor
def metade(valor = 0):
    return valor / 2

def dobro(valor = 0):
    return valor * 2

def aumento(valor = 0):
    valor = valor + (valor * 0.10)
    return valor

def reducao(valor = 0):
    valor = valor - (valor * 0.13) 
    return valor

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')