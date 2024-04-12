# notes - group by and aggregation commands in Pandas
import pandas as pd
df = pd.read_csv(r"C:\Users\colle\Desktop\Pandas Tutorial\Flavors.csv")
df

group_by_frame = df.groupby('Base Flavor')
group_by_frame.mean(numeric_only = True)

df.groupby('Base Flavor').mean(numeric_only = True)

df.groupby('Base Flavor').count()

df.groupby('Base Flavor').min()

df.groupby('Base Flavor').max()

df.groupby('Base Flavor').sum()

df.groupby('Base Flavor').agg({'Flavor Rating' : ['mean', 'max', 'count', 'sum'], 'Texture Rating': ['mean', 'max', 'count', 'sum']})

df.groupby(['Base Flavor', 'Liked']).mean(numeric_only = True)

df.groupby(['Base Flavor', 'Liked']).agg({'Flavor Rating' : ['mean', 'max', 'count', 'sum']})

df.groupby('Base Flavor').describe()
