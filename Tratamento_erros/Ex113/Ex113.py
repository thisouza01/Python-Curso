# menu de cadastros
import interface.interface as interface

# Programa principal
while True:
    interface.mostra_menu()    
    try:
        print()
        escolha = int(input('Escolha uma opção: '))
        print()
    except(ValueError, TypeError):
        print('Erro: Digite uma opção válida!!')
        continue
    except(KeyboardInterrupt):
        print('Interrompido o programa')   
        break 
    else:
        match escolha:
            case 1:
                print('Lista de pessoas')
                import funçoes.ler as listar
                listar.ler_lista()

            case 2:
                print('Cadastro de pessoas')
                try:
                    nome = str(input('Nome: '))
                    idade = int(input('Idade: '))
                except(ValueError, TypeError):
                    print('Digite valores válidos!!')
                else:       
                    import funçoes.cadastro as cadastro
                    cadastro.cadastrar_pessoas(nome, idade)

            case 3:
                print('Sair')
                break

            case _:
                print('Opção invalida!!')

