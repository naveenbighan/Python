import pandas as pd

# !Load the CSV file
df = pd.read_csv('output_data.csv')


df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

df.loc[7, 'Duration'] = 45

df.dropna(subset=['Date'], inplace = True)
print(df.to_string())
print(df.drop_duplicates())


print(df.corr()) 



