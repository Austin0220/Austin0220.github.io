import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

Raw= pd.read_csv('bodyPerformance.csv')
print(Raw.head())
print(Raw.columns)
print(Raw.dtypes)
Raw['muscleMass%(Rough)']= 100-Raw['body fat_%']
print(Raw['muscleMass%(Rough)'])
SortedRaw=Raw.sort_values(by='class')
print(SortedRaw)
#Questions
#What correlation if any is there between body fat and strength?
#how does body fat affect physical fitness?
#What aspects of physical fitness are most impacted by high body fat%?
#What correlation if any is there between age and fitness?

#sns.set(rc={"figure.figsize":(20,12)})
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='gripForce')
#plot= sns.scatterplot(data=Raw, x='weight_kg', y='body fat_%')
#plotting both of these columns in relation to weight shows that there is at least some missing factor here that is making up for the clear discrepancy. 
#two factors make up for dynamic weight (as opposed to static weight being from bones, organs, cartilage which varies marginally with height.) these being fat and muscle.
#the figure shown illustrates that the relationship between body fat and weight does not map to the relationship between grip strength and weight.
#plot2= sns.scatterplot(data=Raw, x='weight_kg', y='muscleMass%(Rough)')
#The data itsef used a ranking system of four ratings, A through D.
#plot3= sns.boxplot(data=SortedRaw, x='class', y='body fat_%')
#figure shows a correlation between class and body fat
plot3= sns.barplot(data=SortedRaw, x='age', y='gripForce')
plt.show()