import pandas as pd
data=pd.read_csv('HollywoodMovies.csv',index_col='Movie')
#first=data['LeadStudio']
#print(first)
#inorder to select multiple columns
first=data[['LeadStudio','Genre','Story','Year']]
print(first.head(43))
