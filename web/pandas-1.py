import pandas as pd
df=pd.read_csv("Data.csv")
#print(df.head())
print(df.sort_values(by="price",ascending=True))