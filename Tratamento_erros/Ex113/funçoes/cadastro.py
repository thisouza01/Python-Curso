def cadastrar_pessoas(nome, idade):
    # cria o arquivo caso não exista e adiciona as pessoas
    with open('arquivo_cadastro.txt', 'at') as arquivo:
        arquivo.write(f'{nome},{idade}\n')