import pandas as pd
data=pd.read_csv('nba1.1.csv')
df=pd.DataFrame(data,index=[0,1,2,3,4,5,6,7,8,9,10,11])
print(df[[True,False,True,False,True,False,True,False,True,False,True,False,]])
#
