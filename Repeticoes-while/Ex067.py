# contadores
maiorIdade = 0
contHomem = 0
contMulher = 0

while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M \ F] '))

    continuar = str(input('Quer continuar? [s \ n] '))

    # verifica maior idade
    if idade >= 18:
        maiorIdade += 1   

    # verifica quantidade homens
    if sexo == 'M':
        contHomem += 1    

    # verifica quantidade mulheres
    if sexo == 'F' and idade < 20:
        contMulher += 1

    # condição saida
    if  continuar == 'n':
        print(f'Tem mais de 18 anos: {maiorIdade} pessoas')
        print(f'Foram cadastrados {contHomem} homens')
        print(f'A quantidade de mulheres com menos de 20 anos é {contMulher}')
        break

  