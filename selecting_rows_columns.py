import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
row=data.iloc[[3,4],[0,2]]
print(row)
