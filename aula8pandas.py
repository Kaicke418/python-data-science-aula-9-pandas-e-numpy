import pandas as pd

dados = pd.read_csv('bestSelling_games.csv')

df = pd.DataFrame(dados)
print(df.head())
print(df.tail())
print(df.loc[0])
print(df.iloc[-1])
