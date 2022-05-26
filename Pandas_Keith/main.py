import pandas as pd
import re

df = pd.read_csv('pokemon_data.csv')
# print(df)
# print(df.head(3))
# print(df.tail(3))
# df_xlsx = pd.read_excel('pokemon_data.xlsx')
# print(df_xlsx)
# df_txt = pd.read_csv('pokemon_data.txt', delimiter = '\t')
# print(df_txt)

# print(df.columns)
# print(df[['Name', 'Generation', 'Legendary',]][0:5])
# print(df.iloc[0:5])
# print(df.iloc[3, 1])

# for index, row in df.iterrows():
# #     print(index, row['Name'])

# print(df.loc[df['Type 1'] == 'Water'])


# Sorting
# print(df.describe())
# print(df.sort_values(["Type 1", "HP"], ascending = [1, 0]))

# df['Total'] = df['HP'] + df['Attack'] + df['Defense'] + df['Sp. Atk'] + df['Sp. Def'] + df['Speed']
# print(df['Total'])
# df = df.drop(columns = ['Total'])
# print(df)

# df['Total'] = df.iloc[:, 4:10].sum(axis=1)
# print(df)
#
# cols = list(df.columns.values)
# df = df[cols[0:4] + [cols[-1]] + cols[4:12]]
# print(df)
#
# df.to_csv("Modified_Pokemons", index = False)
# df.to_excel("Modified_Pokemons.xlsx", index = False)
# df.to_csv("Modified_Pokemons.txt", index = False, sep='\t')

# More Advanced Filtering Data
# new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# new_df.to_csv('Mocne_pokemony', index = False)
# new_df.reset_index(drop = True, inplace = True)
# print(new_df)

# print(df.loc[~df['Name'].str.contains('Mega')])
# print(df.loc[df['Type 1'].str.contains('fire|grass', flags = re.I, regex=True)])
# print(df.loc[df['Name'].str.contains('pi[a=z]*', flags = re.I, regex=True)])

#Conditional Changes

# df.loc[df['Type 1'] == 'Flamer', 'Legendary'] = True
# print(df)

# pd = pd.read_csv('')
# print(df)
#
# df.loc[df['Total'] > 500, ['Generation, Legendary']] = 'TEST VALUE'
# print(df)
# print(df)

#Aggregate Statistics
# df = pd.read_csv('Modified_Pokemons')
# print(df.groupby(['Type 1']).mean().sort_values('Defense', ascending = False))
# print(df.groupby(['Type 1']).sum())
# print(df.groupby(['Type 1']).count())
# df['count'] = 1
# print(df)
# print(df.groupby(['Type 1', 'Type 2']).count()['count'])

#Large amount of data
# df = pd.read_csv('Modified_Pokemons')
#
# new_df = pd.DataFrame(columns=df.columns)
#
# for df in pd.read_csv('Modified_Pokemons', chunksize=5):
#     results = df.groupby(['Type 1']).count()
#
#     new_df = pd.concat([new_df, results])
