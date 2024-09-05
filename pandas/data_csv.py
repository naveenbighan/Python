import pandas as pd

df = pd.read_csv('data.csv')
pd.options.display.max_rows=9999


# print(df.head(10)) 
# print(df.tail()) 
# print(df.info())
# print(len(df))


# df.fillna(100,inplace= True)
# print(df)

# df["Calories"].fillna(101,inplace=True)
x = df["Calories"].mean()

df["Calories"].fillna(x, inplace = True)
print(df)





