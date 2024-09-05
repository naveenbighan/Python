import pandas as pd

data= pd.read_json('hello.json')
print(data.to_string())