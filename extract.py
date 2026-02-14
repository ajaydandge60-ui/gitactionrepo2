import pandas as pd 

print("extract data from mysql")

data ={
    "id":[1,2,3,4,5],
    "name":['a','b','c','d','e'],
    "add":['A','B','C','D','E']
}

df =pd.DataFrame(data)

print(df)
