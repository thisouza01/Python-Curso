def contador(inicio, fim, passo):
    # validação
    if passo == 0:
        passo = 1
    if inicio > fim and passo > 0:
        passo = -passo

    for i in range(inicio, fim, passo):
        print(i, end=' ')  


# mostra de 1 ate 10 de 1 em 1
contador(1,11,1)

print()

# mostra de 10 ate 0 de 2 em 2
contador(10, 0, 2)

print()

# personalizado
contador(-1, 10, 2)