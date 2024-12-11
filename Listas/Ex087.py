# inicia listas
lista_classe = []

while True:
    # reinicia lista
    alunos = []

    # recebe nome e notas do aluno
    aluno = str(input('Nome: '))
    notas = [int(input('Notas: '))for _ in range(2)]

    # media das notas
    media = (notas[0] + notas[1]) / 2

    # coloca aluno na lista de alunos
    alunos.append(aluno)
    alunos.append(notas[:])
    alunos.append(media)

    # coloca a lista de alunos na lista da classe
    lista_classe.append(alunos[:])

    # continuar
    continuar = str(input('Continuar (s / n): '))
    while continuar.strip().lower() not in ('s', 'n'):
        print('Digite um valor válido!')
        continuar = str(input('Continuar (s / n): '))

    # condição de saída
    if continuar.strip().lower() == 'n':
        print(lista_classe)
        break

# segundo loop para ver notas individuais
while True:
    # recebe o nome sem espaços
    indice = str(input('De quem quer ver as notas? (digite "sair" caso nao queira saber mais)')).strip()

    # condição de saída
    if indice.lower() == 'sair':
        break

    # procura na lista o nome
    encontrado = False
    for aluno in lista_classe:
        if aluno[0].lower() == indice.lower():
            print(f'As notas ddo aluno {aluno[0]} são: {aluno[1]}')
            encontrado = True
            break

    if not encontrado:
        print('Aluno não encontrado!')    