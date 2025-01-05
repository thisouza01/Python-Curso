
# recebe valor
def metade(valor = 0, formatado = False):
    resultado = valor / 2
    return resultado if formatado is False else moeda(resultado)

def dobro(valor = 0, formatado = False):
    resultado = valor * 2
    return resultado if formatado is False else moeda(resultado)

def aumento(valor = 0, formatado = False):
    resultado = valor + (valor * 0.10)
    return resultado if formatado is False else moeda(resultado)

def reducao(valor = 0, formatado = False):
    resultado = valor - (valor * 0.13) 
    return resultado if formatado is False else moeda(resultado)

def moeda(valor = 0, moeda = 'R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')