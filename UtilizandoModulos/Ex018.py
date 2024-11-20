# random de alunos e mostre a ordem sorteada

from random import sample

listaAlunos = ['Maria', 'Jose', 'Thiago', 'Gabi', 'Paulo']

ordemSorteada = sample(listaAlunos, k=5)

print('Ordem sorteada: ', ordemSorteada)
