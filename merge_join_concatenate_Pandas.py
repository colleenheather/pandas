import pandas as pd

# merge is good with column names
# join is good with indexes

df1 = pd.read_csv(r"C:\PATH\LOTR.csv")
df1

df2 = pd.read_csv(r"C:\PATH\LOTR 2.csv")
df2

df1.merge(df2) # default inner join

df1.merge(df2, how = "inner", on = ["FellowshipID", "FirstName"])

df1.merge(df2, how = "outer")

df1.merge(df2, how = "left")

df1.merge(df2, how = "right")

df1.merge(df2, how = "cross")

df1.join(df2, on = "FellowshipID", how = "outer", lsuffix = "_Left", rsuffix = "_Right") 

df4 = df1.set_index('FellowshipID').join(df2.set_index('FellowshipID'), lsuffix = "_Left", rsuffix = "_Right", how = "outer") 

pd.concat([df1, df2]) # rather howing the datagrams left and right, it stacks the data frames top and bottom
df4

pd.concat([df1, df2], join = 'outer', axis = 1)
