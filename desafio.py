import statistics as sts
empresas = {
    'empresa1': [2500, 2800, 3000, 9500, 12000],
    'empresa2': [5000, 5200, 5300, 5400, 5500],
    'empresa3': [1000, 2000, 8000, 15000, 20000],
    'empresa4': [3500, 4000, 4200, 4300, 6000],
    'empresa5': [1200, 1500, 1800, 2500, 10000]}

def media(lista):
    return sum(lista)/len(lista)

def moda(lista):
    return sts.mode(lista)

def mediana (lista):
    return sts.median(lista)

def desvio(lista):
    return sts.stdev(lista)

def amplitude(lista):
    return max(lista) - min(lista)

def variancia(lista):
    return sts.variance(lista)

while True:
    escolha = input('escolha entre as empresas ou digite sair para sair: empresa1, empresa2, empresa3, empresa4, empresa5>>')
    if escolha == 'sair':
        print('programa finalizado')
        break

    if empresas[escolha]:
        print(f'''a media dos salarios dessa empresa é {media(empresas[escolha])}\n
                  a moda dos salarios dessa empresa é {moda(empresas[escolha])}\n
                  a mediana dos salarios dessa empresa é {mediana(empresas[escolha])}\n
                  o desvio padrão dos salarios dessa empresa é {desvio(empresas[escolha])}\n
                  a amplitude dos salarios dessa empresa é {amplitude(empresas[escolha])}\n
                  a variancia dos salarios dessa empresa é {variancia(empresas[escolha])}\n''')
   


# ## Desafio 1

# ***Você é um profissional em transição de carreira e está avaliando novas oportunidades de emprego.***

# ***Utilize estatísticas como média, moda, mediana e desvio padrão, amplitude, variância para analisar as faixas salariais oferecidas por diferentes empresas e tomar uma decisão embasada.***

# ***Explique sua escolha com base nos dados analisados***

# ***Verifique isso através dos salários:***



# # #Adicionar comentários: Escolheria a empresa 2 poiss é a que mais me agrada, o salário de 5000 reais seria bom o bastante para trabalhar em uma empresa, seu desvio padrão é baixo e a variância dos salários é de 37000, acho que é uma empresa justa

# # # Qual empresa escolheria?
# # Porquê?
# # O que você entendeu do desvio padrão, média, moda, mediana, amplitude,  variância dessa empresa?
#a média da empresa é alta, a moda de seus salarios é de 5300, a empresa é a que tem o desvio padrão mais baixo das outras e sua variancia indica que ela é bem dispersa