import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn import tree
import statsmodels.api as sm
# NEEDS ABSOLUTE FILE PATH!!! #
Raw= pd.read_csv("C:\\Users\\Cranell\\Documents\\GitHub\\Austin0220.github.io\\itcs3162\\projectfiles\\Project 2\\bodyPerformance.csv")
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
X=RefRaw.drop(columns=['class_D', 'class_B', 'class_C', 'class_A'])
#y=RefRaw['class_D']
#y=RefRaw['class_C']
y=RefRaw['class_B']
#y=RefRaw['class_A']
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=.30)
print(X_train.shape, X_test.shape, y_train.shape, y_test.shape)
clf= tree.DecisionTreeClassifier()
clf=clf.fit(X_train, y_train)
print(clf.predict(X_test))
predicted=clf.predict(X_test)
print(clf.score(X_test, y_test), predicted)
fig=plt.figure(figsize=(60,80))
_= tree.plot_tree(clf, feature_names=X.columns, filled=True, max_depth=3)
#tree.plot_tree(clf, feature_names=X.columns, filled=True)
#print(SortedRaw)
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='gripForce')
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='body fat_%')
#plot3= sns.boxplot(data=SortedRaw, x='class', y='body fat_%')
#figure shows a correlation between class and body fat
#plot3= sns.barplot(data=SortedRaw, x='age', y='gripForce')
plt.show()
fig.savefig('C:\\Users\\Cranell\\Documents\\GitHub\\Austin0220.github.io\\itcs3162\\projectfiles\\Project 2\\figure4B.png')