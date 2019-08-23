import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
first=data.ix['Spider-Man 3']
print(first)
#using integer format
second=data.ix[1]
print(second)
