import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
first=data.loc[:,['LeadStudio','RottenTomatoes','Story']]
print(first)
