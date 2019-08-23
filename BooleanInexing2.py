import pandas as pd
dict={'name':['aparna','pankaj','shudhir','shoha'],
      'degree':['MBA','BCA','M.tech','MBA'],
      'Score':[90,40,80,98]}
df=pd.DataFrame(dict,index=[True,False,True,False])
print(df.iloc[2])
