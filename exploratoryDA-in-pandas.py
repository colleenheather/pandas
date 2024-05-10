import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\colle\Desktop\Pandas Tutorial\world_population.csv")
df

pd.set_option('display.float_format', lambda x: '%.2f' % x) # reformat
df.info()

df.describe() # returns count, mean, std, min percentages, max

df.isnull().sum() # returns count in each column

df.nunique() # how many unique values in each column

df.sort_values(by="2022 Population", ascending=False).head(10) #head gives top values

df.corr(numeric_only=True)

# visualize with heatmap
sns.heatmap(df.corr(numeric_only=True), annot = True)
plt.rcParams['figure.figsize'] = (20, 7)
plt.show()

# group data together

df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)

df[df['Continent'].str.contains('Oceania')]

# df2 = df.groupby('Continent')[['2022 Population',
#        '2020 Population', '2015 Population', '2010 Population',
#        '2000 Population', '1990 Population', '1980 Population',
#        '1970 Population']].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)

df2 = df.groupby('Continent')[df.columns[5:13][::-1]].mean(numeric_only=True).sort_values(by="2022 Population", ascending=False)
df2 

df3 = df2.transpose() 
df3

df2.plot()

df3.plot()

df.boxplot(figsize=(20,10)) # finding outliers 

df.dtypes

df.select_dtypes(include='number') # returning columns of data frame with number data type

df.select_dtypes(include='object')

df.select_dtypes(include="float")

