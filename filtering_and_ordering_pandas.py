# notes - some commands on how to order and filter in Pandas

import pandas as pd

df = pd.read_csv(r"PATH\world_population.csv")
df

df[df['Rank'] <= 10]

specific_countries = ['Bangladesh', 'Brazil']
df[df['Country'].isin(specific_countries)]

df[df['Country'].str.contains('United')]

df2 = df.set_index('Country')
df2

df2.filter(items = ['Continent', 'CCA3'])

df2.filter(items = ['Zimbabwe'], axis = 0)

df2.filter(like = 'United', axis = 0)

df2.loc['United States']

df2.iloc[3]

df[df['Rank'] < 10].sort_values(by=['Continent', 'Country'], ascending=[False, True])
