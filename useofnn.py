import pickle as p
import pandas as pd
import math
df = pd.read_csv('try.csv')
target_column = ['costLS']
predictors = list(set(list(df.columns))-set(target_column))
m=df[target_column].max()
loadmodel=p.load(open('finaln.pkl','rb'))
par1=[2, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1]
par1=par1/df[predictors].max()
res=loadmodel.predict([par1])
n=float(m)
r=float(res)
print(math.floor(r*n))