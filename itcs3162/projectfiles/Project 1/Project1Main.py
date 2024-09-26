import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Raw= pd.read_csv('E:\\Documents\\GitHub\\Austin0220.github.io\\itcs3162\\projectfiles\\Project 2\\bodyPerformance.csv')
print(Raw.head())
print(Raw.columns)
print(Raw.dtypes)
Raw['muscleMass%(Rough)']= 100-Raw['body fat_%']
print(Raw['muscleMass%(Rough)'])
SortedRaw=Raw.sort_values(by='class')
print(SortedRaw)
#Premise

plt.show()