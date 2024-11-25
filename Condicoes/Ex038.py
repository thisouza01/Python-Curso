# ler duas notas, calcular media, < 5 reprovado, >= 5 and <= 6.9 recuperação, >= 7 aprovado

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

# calculo da media
media = (nota1 + nota2) / 2

# verificação do status do aluno
if media < 5:
    print('Reprovado!')
elif media >= 5 and media <= 6.9:
    print('Recuperação!')    
elif media > 6.9:
    print('Aprovado!')