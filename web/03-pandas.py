
import pandas as pd 
df=pd.read_csv("Data.csv")
# print(df.head()) #top 5 rows
# print(df.columns) #columns
# print(df.describe()) #summary statistics

# print(df[df["price"]>32000]) #filter

sort=df.sort_values(by="price",ascending=False) #sorting
print("\n Sorted date: ",sort)