import pandas as pd
import numpy as np
import sys
import pickle
import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates
from sklearn.neural_network import MLPRegressor

# Import necessary modules
from sklearn.model_selection import train_test_split

from math import sqrt
from sklearn.metrics import r2_score
from sklearn.utils import column_or_1d
#قراءة بيانات
df = pd.read_csv('dataff.csv')
#تحديد العمود الهدف(النتيجة)
target_column = ['costLS']
#نورملايز لله
#اقصاء العمود الهدف والباقي تخزينه في مصفوفة الميزات
predictors = [ "Areaoftypicalfloor","UseOfBuilding","NoFloors","FootingType"]
#نورملايز للميزات
#df[predictors] = df[predictors]/df[predictors].max()
#print(df[predictors].max())
#print(df.describe().transpose())
print(df.shape)
#print(df.describe().transpose())
X =df[predictors].values
y =df[target_column ].values
#y = column_or_1d(y, warn=True)
#data_norm=pd.concat(X_norm[[predictors ,target_column]],axis=1)
#parallel_coordinates(data_norm, 'class')
plt.scatter(df["Mechanicaltype"], y, color = 'red')
plt.title('Cost vs "Mechanicaltype"')
plt.xlabel('parameter')
plt.ylabel("UseOfBuilding")
plt.show()
