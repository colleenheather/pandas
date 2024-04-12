# notes
# indexes are objects that store the axis labels for all pandas objects 
import pandas as pd
df = pd.read_csv(r"PATH\world_population.csv", index_col = "Country")
df

df.reset_index(inplace=True) # reset to default numbers
df

df.set_index('Country', inplace = True) # inplace saves it
df

df.loc['Albania'] # same as df.iloc[1]

df.reset_index(inplace = True)

df.set_index(['Continent', 'Country'], inplace = True)

pd.set_option('display.max.rows', 235)
df.sort_index()

df.loc['Africa', 'Angola'] # loc can specify multiple indexing
df.iloc[1] #iloc works with inital index
