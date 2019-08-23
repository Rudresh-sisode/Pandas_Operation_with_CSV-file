import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
row=data.iloc[3];
print(row)
#mulitiple rows
row2=data.iloc[[3,6,8]]
print(row2)
