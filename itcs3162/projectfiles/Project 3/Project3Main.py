import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn import tree
import statsmodels.api as sm
# NEEDS ABSOLUTE FILE PATH!!! #
Raw= pd.read_csv("C:\\Users\\Cranell\\Documents\\GitHub\\Austin0220.github.io\\itcs3162\\projectfiles\\Project 3\\bodyPerformance.csv")
print(Raw.head())
print(Raw.columns)
print(Raw.dtypes)
print(Raw.isna().sum())
#Raw['muscleMass%(Rough)']= 100-Raw['body fat_%']
#print(Raw['muscleMass%(Rough)'])
SortedRaw=Raw.sort_values(by='class')
#sns.countplot(data=Raw, x='class')
RefRaw = pd.get_dummies(Raw , drop_first=False)
print(RefRaw)
RefRaw = RefRaw.drop(columns = )
X=RefRaw.drop(columns=['class_D', 'class_B', 'class_C', 'class_A'])
#y=RefRaw['class_D']
#y=RefRaw['class_C']
#y=RefRaw['class_B']
Y=RefRaw['class_A']
print(X)
print(Y)
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.2, random_state =0)
print(X_train.shape, X_test.shape, Y_train.shape, Y_test.shape)
reg = LinearRegression()
reg.fit(X_train, Y_train)
print(reg.score(X_test, Y_test))
Y_pred1 = reg.predict(X_test)
mae1 = mean_absolute_error(Y_test, Y_pred1).round(2)
mse1 = mean_squared_error(Y_test, Y_pred1).round(2)
mape1 = ((np.mean(np.abs(Y_test-Y_pred1)/Y_test) * 100)/((len(RefRaw))+1)).round(2)

print(f"MAE: {mae1}\n MSE:{mse1} \n MAPE:{mape1}%.")
#print(clf.predict(X_test))
#predicted=clf.predict(X_test)
#print(clf.score(X_test, Y_test), predicted)
fig=plt.figure(figsize=(60,80))
#_= tree.plot_tree(clf, feature_names=X.columns, filled=True, max_depth=3)
#tree.plot_tree(clf, feature_names=X.columns, filled=True)
#print(SortedRaw)
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='gripForce')
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='body fat_%')
#plot3= sns.boxplot(data=SortedRaw, x='class', y='body fat_%')
#figure shows a correlation between class and body fat
#plot3= sns.barplot(data=SortedRaw, x='age', y='gripForce')
#plt.show()
#fig.savefig('C:\\Users\\Cranell\\Documents\\GitHub\\Austin0220.github.io\\itcs3162\\projectfiles\\Project 2\\figure4B.png')