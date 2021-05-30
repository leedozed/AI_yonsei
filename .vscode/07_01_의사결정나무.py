#%%
import pandas as pd
import numpy as np
from statsmodels.graphics.mosaicplot import mosaic
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import tree
titanic = pd.read_csv("titanic.csv")
# print(titanic)

#crosstabl 표 만들기: (열, 행)
pd.crosstab(titanic['Survived'], titanic['Sex']) 
# print(pd.crosstab(titanic['Survived'], titanic['Sex']) )

pd.crosstab(titanic['Survived'], titanic['Class'])
pd.crosstab(titanic['Survived'], titanic['Age'])


mosaic(titanic, ["Age","Survived"])
mosaic(titanic, ["Sex","Survived"])
mosaic(titanic, ["Class","Survived"])
# plt.show()

# factor to number
titanic.Survived = titanic.Survived.replace('No', 0)
titanic.Survived = titanic.Survived.replace('Yes', 1)

titanic.Age = titanic.Age.replace('Child', 0)
titanic.Age = titanic.Age.replace('Adult', 1)

titanic.Sex = titanic.Sex.replace('Male', 0)
titanic.Sex = titanic.Sex.replace('Female', 1)

titanic.Class = titanic.Class.replace('First', 1)
titanic.Class = titanic.Class.replace('Second', 2)
titanic.Class = titanic.Class.replace('Third', 3)
titanic.Class = titanic.Class.replace('Crew', 4)

# Data for tree modeling
X = titanic.drop('Survived', axis = 1)
y = titanic['Survived']
xname = X.columns
yname = ['Die','Survive']

# Decision Tree
DT = tree.DecisionTreeClassifier(max_depth = 3, min_impurity_decrease=0.003)
DT_fit = DT.fit(X, y)
plt.subplots(figsize=(11, 9))
tree.plot_tree(DT_fit, feature_names=xname, class_names=yname, filled=True)


