# ## ***Desafio 2***

 

# ***VOCÊ É UM DESENVOLVEDOR E PRECISA IMPLEMENTAR UM SISTEMA PARA UMA INSTITUIÇÃO DE ENSINO.***

# ***O SISTEMA DEVE GERENCIAR AS NOTAS DOS ESTUDANTES, APRESENTANDO ESTATÍSTICAS COMO MODA, MÉDIA, MEDIANA, AMPLITUDE DESVIO PADRÃO. ALÉM DISSO, DEVE IDENTIFICAR A MENOR E A MAIOR NOTA. ORGANIZE O CÓDIGO EM MÓDULOS E SEPARE AS FUNCIONALIDADES EM FUNÇÕES DISTINTAS.***

# ***1 - USAR STATISTICS***

# ***2 - UTILIZE MÓDULOS SEPARADOS***

# ***3 - Utilize Parâmetros, caso deixe mais flexível***

# 4 - Extraia os dados de todos os alunos
import analise as an

alunos = {
    'Ana': [5, 7, 8, 9, 9, 10, 10, 10],
    'Carlos': [4, 7, 8, 7, 7, 8, 9, 2],
    'David': [3, 3, 3, 6, 7, 4, 4, 4],
    'Emanuelly': [8, 8, 9, 10, 10, 10, 9, 9],
    'Emili': [10, 9, 10, 10, 10, 9, 9, 10],
    'Igor': [2, 2, 3, 5, 5, 5, 6, 6],
    'Iara': [5, 3, 8, 7, 7, 5, 5, 6],
    'João': [7, 8, 8, 8, 8, 6, 5, 5],
    'Kevin': [1, 4, 5, 3, 2, 8, 8, 6]
}
print('escolha um aluno entre')
for chave in alunos.keys():
    print(chave)

while True:
   
    select = input('escolha um aluno ou digite sair para sair>> ')

    if select == 'sair':
        print('programa finalizado')
        break

    if select in alunos:
        print(f'''a média do aluno(a) {select}, é {an.media(alunos[select])}
              a moda do aluno(a) é {an.moda(alunos[select])}
              a mediana do aluno(a) é {an.mediana(sorted(alunos[select]))}
              o desvio padrão do aluno(a) é {an.desvio(alunos[select])}
              a variância do(a) aluno é {an.variancia(alunos[select])}
              a amplitude do(a) aluno é {an.amplitude(alunos[select])}
              a maior nota é {max(alunos[select])}
              a menor nota é {min(alunos[select])}''')
