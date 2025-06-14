import statistics

clientes = [
{"Idade": 45, "Limite": 12691, "Meses_cliente": 39, "Taxa_utilizacao": 0.061},
{"Idade": 49, "Limite": 8256, "Meses_cliente": 44, "Taxa_utilizacao": 0.105},
{"Idade": 51, "Limite": 3418, "Meses_cliente": 36, "Taxa_utilizacao": 0},
{"Idade": 40, "Limite": 3313, "Meses_cliente": 34, "Taxa_utilizacao": 0.76},
{"Idade": 40, "Limite": 4716, "Meses_cliente": 21, "Taxa_utilizacao": 0},
{"Idade": 44, "Limite": 4010, "Meses_cliente": 36, "Taxa_utilizacao": 0.311},
{"Idade": 51, "Limite": 34516, "Meses_cliente": 46, "Taxa_utilizacao": 0.066},
{"Idade": 32, "Limite": 29081, "Meses_cliente": 27, "Taxa_utilizacao": 0.048},
{"Idade": 37, "Limite": 22352, "Meses_cliente": 36, "Taxa_utilizacao": 0.113},
{"Idade": 48, "Limite": 11656, "Meses_cliente": 36, "Taxa_utilizacao": 0.144},
{"Idade": 42, "Limite": 6748, "Meses_cliente": 31, "Taxa_utilizacao": 0.217},
{"Idade": 65, "Limite": 9095, "Meses_cliente": 54, "Taxa_utilizacao": 0.174},
]

idades = [c['Idade'] for c in clientes]
limites =[c['Limite'] for c in clientes]
meses_clientes = [c['Meses_cliente'] for c in clientes]
taxa_utilizacao = [c['Taxa_utilizacao'] for c in clientes]


def analisar(dados, nome):
    print(nome)
    print('Media', statistics.mean(dados))
    print()
    print('Mediana', statistics.median(dados))
    print()
    print('Desvio', statistics.stdev(dados))
    print()

    if nome == 'Taxa_utilizacao':
       zeros = taxa_utilizacao.count(0)
       print(f'Clientes Inativos(0% utilização), {zeros/len(taxa_utilizacao)}, {zeros/len(taxa_utilizacao)}')

analisar(idades,'Idades')
analisar(limites,'Limite')
analisar(meses_clientes,'Meses_cliente')
analisar(taxa_utilizacao ,'Taxa_utilizacao')

# insight

# pessoas na faixa 40 > <= 55
# carreira solicitada
# Permaneram um tem consideravel com o cartão
# a taxa de utilização extremamente baixa

# tomada de decisão
# tomada de decisão 
# pesquisa mkt 
# publicidade 
# insentivo  






