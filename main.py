import pandas as pd
import os

df = pd.read_excel('./data/Superstore.xlsx')
df_final = df.iloc[:10, 0:4]

path = os.path.dirname(os.path.realpath(__file__))
df_final.to_csv(f'{path}/data/Superstore.csv', index=False)

print(f'Exporting to {path}/data/Superstore.csv')
print(df_final)
print('bye')