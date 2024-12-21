def fatorial(numero = 1, show = False):
    # inicia resultado da soma
    resultado = 1
    
    # fatorial
    for i in range(numero, 0, -1):
        resultado *= i      
        # mostra o passo a passo, apenas se for verdade
        if show == True:
            print(f'{i}', end=' x ' if i > 1 else ' = ')

    # mostra resultado
    print(resultado)

fatorial(5)
fatorial(5, True)
