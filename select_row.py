import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
first=data.loc[['Juno','Enchanted'],['LeadStudio','Story','Genre']]
print(first)

