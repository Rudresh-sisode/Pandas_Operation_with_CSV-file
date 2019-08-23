import pandas as pd
data=pd.read_csv('nba-2.csv',index_col='Name')
print(data['Age']>25)
