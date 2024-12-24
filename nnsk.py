import pandas as pd
import numpy as np
import sys
import pickle

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
#نورملايز للهدف
df[target_column ]=df[target_column ]/df[target_column ].max()
#اقصاء العمود الهدف والباقي تخزينه في مصفوفة الميزات
#predictors = list(set(list(df.columns))-set(target_column))
predictors = [ "Areaoftypicalfloor","UseOfBuilding","NoFloors","FootingType"]
#نورملايز للميزات
df[predictors] = df[predictors]/df[predictors].max()
#print(df[predictors].max())
#print(df.describe().transpose())
print(df.shape)
#print(df.describe().transpose())
X =df[predictors].values
y =df[target_column ].values
#y = column_or_1d(y, warn=True)
y=y.ravel()
print(X)
#data = df.to_dict('records')  # retb
#تقسيم البيانات لتدريب و اختبار
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=40)
print(X_train.shape); print(X_test.shape)


#انشاء الشبكة العصبية
mlp=MLPRegressor(hidden_layer_sizes=(17,17),activation="tanh",solver='sgd',max_iter=650)
# تدريب الشبكة العصبية
mlp.fit(X_train,y_train)
#حفظ نتيجة التدريب كملف بايكل
filen='finaln1.pkl'
pickle.dump(mlp,open(filen,'wb'))
# التنبؤ لبيانات التدريب
predict_train = mlp.predict(X_train)
#التنبؤ لبيانات الاختبار
predict_test = mlp.predict(X_test)
# تضمين المكتبة يلي فيها الدالة يلي بتحسب المتوسط للخطأ
from sklearn.metrics import mean_squared_error
#تعليمة طباعة للجملة cost of traning
print('cost of traning')
#حساب متوسط الخطأ للتنبؤ (بيانات التدريب) و طباعته
print(mean_squared_error(predict_train,y_train))
#حساب و طباعة متوسط الخطأ لبيانات الاختبار
print('cost of test')
print(mean_squared_error(predict_test,y_test))
#m1=mlp.predict([[1,2,1,1,2,0,0,0,2,1,1]])
#print(m1)