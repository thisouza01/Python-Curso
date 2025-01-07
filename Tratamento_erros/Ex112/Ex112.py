# menu de cadastros
import interface.interface as interface
# Programa principal
while True:
    interface.mostra_menu()    
    try:
        escolha = int(input('Escolha uma opção: '))
    except(ValueError, TypeError):
        print('Erro: Digite uma opção válida!!')
        continue
    except(KeyboardInterrupt):
        print('Interrompido o programa')   
        break 
    else:
        match escolha:
            case 1:
                print('Opção 1') 
            case 2:
                print('Opção 2')
            case 3:
                print('Opção 3')
                break
            case other:
                print('Opção invalida!!')

