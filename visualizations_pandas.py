import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\colle\Desktop\Pandas Tutorial\Ice Cream Ratings.csv")
df = df.set_index('Date')
df

print(plt.style.available) # shows the available styles to change up visualization
plt.style.use('seaborn-v0_8')

df.plot() # inside parenthesis shift tab to see options 
# (kind = 'line') is default

df.plot(kind = 'line', subplots = True) # lines are broken up into individual graphs rather being in same visualization

df.plot(kind="line", title = "Ice Cream Ratings", xlabel = "Daily Ratings", ylabel = "Scores")

df['Flavor Rating'].plot(kind = "bar", stacked = True)

df.plot.barh(stacked = True) # horizontal bar chart

df.plot.scatter(x = 'Texture Rating', y = 'Overall Rating', s = 300, c = 'red') # must specify x and y axis

df.plot.hist(bins = 20)

df.boxplot()

df.plot.area(figsize = (10, 5))

df.plot.pie(y = "Flavor Rating", figsize = (10,6)) # must specify column 
