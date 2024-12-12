#ler nome e media de u aluno e mostrar se pasou ou foi reprovado
# inicia lista de alunos
alunos = []

while True:    
    # recebe dados
    aluno = {
        "nome": str(input('Nome do aluno: ')),
        "media": float(input(f'Média do aluno: '))
    }

    # envia os dados do aluno para lista de alunos
    alunos.append(aluno)

    # continuar?
    continuar = str(input('Quer continuar? (s / n) : '))
    while continuar.strip().lower() not in ('s', 'n'):
        print('Digite uma opção válida!')
        continuar = str(input('Quer continuar? (s / n) : '))

    # condição de saída
    if continuar.lower().strip() == 'n':
        
        for item in alunos:
            # verifica se foi aprovado ou reprovado
            print('-----------------------')
            if item['media'] >= 7:
                print(f"{item['nome']} foi aprovado com média {item['media']}.")
            else:
                print(f"{item['nome']} foi reprovado com média {item['media']}.")
        break