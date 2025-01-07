def ler_lista():
    with open('arquivo_cadastro.txt', 'r') as arquivo:
        lido = arquivo.read()
        print(f'\n{lido}\n')