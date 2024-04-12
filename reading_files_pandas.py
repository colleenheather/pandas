import pandas as pd
pd.set_option('display.max.rows', 235)
pd.set_option('display.max.columns', 40)

df = pd.read_csv(r"CSV FILE PATH")
# , header = None, names = ['Country', 'Region'])
df


#df2 = pd.read_csv(r"C:\Users\colle\Desktop\Pandas Tutorial\countries of the world.txt", sep = '\t')
df2 = pd.read_table(r"C:\Users\colle\Desktop\Pandas Tutorial\countries of the world.txt")
df2

df3 = pd.read_json(r"JSON FILE PATH")
df3


df4 = pd.read_excel(r"EXCEL FILE PATH", sheet_name = "Sheet2")
# will use the first sheet as default
df4

df2.info()
df2.shape
df2.head(10)
df2.tail(10)
df2.loc[224] 
df2.iloc[224] # integer location


