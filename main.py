import pandas as pd

df = pd.read_excel('./data/Superstore.xlsx')
df_final = df.iloc[:10, 0:4]

df_final.to_csv('./data/Superstore.csv', index=False)
print(df_final)
print('bye')